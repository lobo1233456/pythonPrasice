import random
import time

from flask import Flask, jsonify, request, Response
import sqlite3

# 因为有些异常情况的时候需要提示异常信息，所以咱们需要事先定义一些错误信息，以及错误码
# 请求方式错误
method_err = {
    "code": 301,
    "msg": "请求方式不正确，只支持post请求"
}
# 参数错误
param_err = {
    "code": 302,
    "msg": "请求参数错误，请检查入参"
}
# 余额不足
money_err = {
    "code": 303,
    "msg": "账户余额不足"
}

# 价格错误
price_err = {
    "code": 304,
    "msg": "价格不合法"
}

# 用户不存在
user_err = {
    "code": 305,
    "msg": "该用户不存在"
}

# 成功的信息
success_msg = {
    "code": 200,
    "msg": "支付成功"
}

# 数据库异常
db_err = {
    "code": 306,
    "msg": "数据库错误"
}

# 导入我们需要用到的模块，Flask是用来创建我们写的这个接口的服务
# jsonify是用来序列化json的，因为http_api接口都是返回的json串
# request是用来获取调用接口的时候传入的数据，这几个模块都是falsk里面的


app = Flask(__name__)
# 这个是初始化一个服务，__name__代表是咱们写的这个python文件,
# 也就是咱们这个python文件就是一个服务了，然后赋值给app，app就代表这个服务了

app.config['JSON_AS_ASCII'] = False


# 支付的时候，传入金额，金额可能有小数类型的，也可能有整数类型的
# 因为python里面没有一个内置的方法去判断字符串是不是小数，所有下面自己写了
# 一个方法去校验是否为正小数
def check_float(string):
    str1 = str(string)
    if str1.count('.') > 1:  # 判断小数点是不是大于1
        return False
    elif str1.count('-') > 0:  # 判断负号的个数，如果大于0就是非法的
        return False
    elif str1.isdigit():
        return False  # 判断是不是整数
    else:
        new_str = str1.split('.')  # 按小数点分割字符
        frist_num = new_str[0]  # 取分割完之后这个list的第一个元素
        if frist_num.isdigit() and new_str[1].isdigit():
            # 如果小数点两边都是整数的话，那么就是一个小数
            return True
        else:
            return False


# 因后面要经常操作数据，咱们就写一个函数专门来操作数据库
def op_db(sql):
    db = sqlite3.connect(r'D:\dbsql\mocktest.db')  # 指定数据库
    course = db.cursor()  # 创建游标
    try:  # 捕捉异常,如果有sql写的不对就返回异常
        course.execute(sql)  # 执行sql
    except sqlite3.Error as e:
        # 出异常了就返回错误信息
        return False
    else:
        res = course.fetchone()
        # 获取查询结果
        db.commit()
        return res
        # 返回数据
    finally:
        # 不管出没出异常都关闭数据库
        course.close()
        db.rollback()  # 回滚
        db.close()


def check_balance(user_id, price):
    select_sql = 'select money from accounts where user_id = %s;' % user_id
    data = op_db(select_sql)  # 获取sql执行的结果
    if data:  # 如果返回的数据不是空的话
        if not data:
            # not就是取反的意思，如果返回False的话，就是真了，就说明出错了，返回数据库错误
            return db_err
        else:  # 如果select有结果的话，就获取到这个用户的账号信息
            money = data[0]  # 数据库获取到的结果是一个元组，就一个元素就是价格
            if money >= price:  # 如果账户余额大于等于价格的话，修改价格
                target_money = money - price
                # 更新余额的sql
                update_sql = 'update accounts set money = %s where user_id = %s;' % (target_money, user_id)
                op_db(update_sql)  # 更新余额
                return success_msg  # 返回成功信息
            else:  # 如果余额不足的话，返回余额错误信息
                return money_err
    else:  # 如果数据是空，就是用户信息获取不到
        return user_err


# 这个是给咱们刚才创建的服务加一个路由，也就是指定这个接口的访问url，
# 支持什么请求方式，get或者post请求,route方法第一个参数就是访问的路径，
# methods是支持哪种类型的请求，route方法是一个装饰器，必须写在业务逻辑的函数上面
@app.route('/pay', methods=['POST', 'GET'])
def pay():
    # def pay()就是定义一个函数，这个函数里面写的就是接口的业务逻辑了
    if request.method != 'POST':  # 如果不是post请求的话，返回请求类型错误
        return jsonify(method_err)
        # return 就返回数据了，jsonify就是把python里面的数据类型（字典、list）转成json串
    else:
        user_id = request.values.get('user_id')
        # 使用request.values.get获取到传入的参数，user_id
        price = request.values.get('price')
        # 获取到支付的价格
        if user_id and price:
            # 判断两个入参是否都传了，user_id和price
            if price.isdigit():  # 如果价格是整数的话
                price = int(price)
                # 接收过来的入参是字符串类型的，所以要转成int类型的，才可以加减
            elif check_float(price):
                # 这里调用了一个函数，在上面定义了，是校验传入的价格是不是小数的
                price = float(price)
            else:  # 如果不是整数也不是小数，返回价格错误
                return jsonify(param_err)
            # 上面都校验通过之后，数据就是合法的，就得扣钱了，那就是操作数据库
            # 再写一个函数专门用来扣钱
            res = check_balance(user_id, price)  # 调用检查余额函数

            return jsonify(res)  # 返回结果
        else:  # 如果name或者价格获取不到的话，返回参数错误
            return jsonify(param_err)

def random_str():
    # 待选随机数据
    data = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"

    # 用时间来做随机播种
    random.seed(time.time())

    # 随机选取数据
    sa = []
    for i in range(8):
        sa.append(random.choice(data))
    salt = ''.join(sa)

    return salt


# 构建response
def make_response():
    content = '{"result": "%s", "data": "%s"}' %(random_str(), random_str())
    resp = Response(content)
    resp.headers["Access-Control-Origin"] = '*'
    return resp


# http GET
@app.route("/query", methods=["GET"])
def query():
    return jsonify(
        username=random_str(),
        password=random_str()
    )


# http POST
@app.route("/update", methods=["POST"])
def update():
    return make_response()


# http delete
@app.route("/delete", methods=["DELETE"])
def delete():
    return make_response()


# http head
@app.route("/head", methods=["HEAD"])
def head():
    return make_response()


if __name__ == '__main__':
    app.run(debug=True,port=5001)  # 运行程序，debug的意思是调试模式运行，可以看到请求，默认端口号是5000，可以使用port参数指定端口号

#运行完之后会显示这样的
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# * Restarting with stat
# * Debugger is active!
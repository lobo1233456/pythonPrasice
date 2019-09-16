import pymysql

# 与数据库建立连接
connect_obj = pymysql.connect(host='192.168.2.45',user='root',password='testuser',database='fy_cms',port=3306)
cur = connect_obj.cursor()  # 获取游标


sql = 'select * from message'
count = cur.execute(sql)  # 执行mysql语句
print('共查出',count,'条数据')
ret = cur.fetchall()  # 获取结果中的所有行


#  cur.fetchmany(5)  # 获取结果中的下面5行
#  cur.fetchone()  #  获取结果中的下一行

for i in ret:
    print(i)

# 关闭连接
cur.close()
connect_obj.close()



#-*- coding:utf-8 -*-
import sqlite3
#操作sqlite使用sqlite3模块，上面是导入这个模块
db = sqlite3.connect('D:\dbsql\mocktest.db')
#连接数据库，指定数据库的路径，如果数据库的路径和这个python文件在同一个路径下的话，直接写名字就可以了
#如果不在同一个路径的话，就写数据库文件的绝对路径，例如这样的C:\Users\Sabri\Desktop\my.db
course = db.cursor()
#创建游标，就相当于创建一个数据库里面的工作人员去工作，从数据库里拿东西改东西一样
course.execute(r'select * from accounts;')
#游标执行sql语句，相当于让刚才创建的那个工作人员去执行sql语句
res = course.fetchall()
#获取sql执行结果，保存到res里面，res里面就是sql的执行结果
print(res)
#打印结果
course.close()
#关闭游标
db.commit()
#提交数据库事物，如果是update、insert、delete语句的话需要commit一下才可以生效，select不需要
db.close()
#做人有始有终，有打开就有关闭，关闭数据库连接
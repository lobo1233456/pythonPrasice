# Python基础
#
#     文件操作
#         1.有一个jsonline格式的文件file.txt大小约为10K
#         2.补充缺失的代码
#     模块与包
#         3.输入日期， 判断这一天是这一年的第几天？
#         4.打乱一个排好序的list对象alist？
#     数据类型
#         5.现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
#         6.字典推导式
#         7.请反转字符串 "aStr"?
#         8.将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
#         9.请按alist中元素的age由大到小排序
#         10.下面代码的输出结果将是什么？
#         11.写一个列表生成式，产生一个公差为11的等差数列
#         12.给定两个列表，怎么找出他们相同的元素和不同的元素？
#         13.请写出一段python代码实现删除list里面的重复元素？
#         14.给定两个list A，B ,请用找出A，B中相同与不同的元素
from functools import reduce

# A = [1,2,3]
# B = [3,4,5]
# a = -123213423414
# a = list(str(a)+'asdfs')
# # a = a[::-1]
# # a = ''.join(a)
# print(a)
# result = reduce(lambda x,y:y+x,a)
# print(result)
# A1 = set(A)
# B1 = set(B)
# print(list(A1&B1))
# d= {'a':24,'g':52,'i':12,'k':33}
# res = sorted(d.items(),key=lambda x:x[1])
# print(res)
# a = range(5)
# a = -123213423414
# if a>=0:
#     a = list(str(a) )
#     result= a[::-1]
#     # result = reduce(lambda x, y: y + x, a)
#     print(result)
# else:
#     a = list(str(abs(a)) )
#     # result = reduce(lambda x, y: y + x, a)
#     result = a[::-1]
#     result = ''.join(result)
#     print(result)
#     # print(int('-'+result))

a,b,n = 0,1,0
for i in  range(4):
    a,b = b,a + b
    n = n+1
    print(b)
a= [1,2,3]

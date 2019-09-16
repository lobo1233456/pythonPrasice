# class lalla():
#     @classmethod
#     def la(self):
#         return  ('hello')
# a = [1,2,2,3,4]
# s = "ajldjlajfdljfddd"
# list  = list(set(s))
# list= list.sort(reverse=False)
# print(list)
# res = ''.join(list)
#
# a = [1,2,3,4,5]
# res = []

# b = map(lambda x: x ** 2,a)
#
# a = filter(lambda x: x > 10, b)
# for item in a:
#     res.append(item)
#
#
# print(res)

# b = lambda x,y: x * y
# print(b(3,2))
#
# 24、字典根据键从小到大排序
# #
# import re
#
# dict1={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
# listKey = list(dict1.keys())
# listKey.sort()
# print(listKey)
# listValueNew = []
# for i in listKey:listValueNew.append(dict1[i])
# print(listValueNew)
# newDict = dict(zip(listKey,listValueNew))
# print(newDict)
# a = [1,2,33,33,4]
# b=[1,2,3,4,5,63,3,333]
# c = a + b
# c.sort(reverse=True)
# print(c)
# url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
# resRes = re.findall(r'eRange=(.*?)%7C2',url)
# print(resRes)
#
# list3=[2,3,5,4,9,6,6]
# listnew = []
# for i in list3:
#     for y in list3:
#         if i<y:listnew.append(y)
# print(list(set(listnew)))
#
# s = "ajldjlajfdljfdxdd"
# list  = list(set(s))
# print(list)
# list.sort()
# print(list)

# str ='123'
# enp = int(str)
# print(enp)
# print(type(enp))
# def checkTrue():
#     casePassSuc = True
#     caseCrashSuc = True
#     allsuc = caseCrashSuc and  casePassSuc
#     print(casePassSuc, caseCrashSuc)
#     print(allsuc)
#     return (allsuc)
# checkTrue()
# kwarg='123'
# kwargs={"1":1,"2":3}
# name = 2
# def test(*kwarg,**kwargs):
#
#     print(kwargs)
#     print(kwarg)
# test(kwarg,kwargs,name)
a,b = 1,1
for i in range(10):
    a,b = b,a+b
    print(a)

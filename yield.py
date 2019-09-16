#!user/bin/env python3
# -*- coding: UTF-8 -*-
def genter():
    a = 4
    b = 5
    c = 6
    for i in range(5):
        yield a
        print('hhh'+str(i))
        yield b
        print("aaa" + str(i))
        yield c

# 包含了yield 的 genter() 就是一个生成器
res = genter()
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())

# for  c in enumerate(res):
#     # if i > 1:
#     #     # 通过 break 来测试执行的结果
#     #     break
#     print(c)
# a = [1,2,3,4]
# b = 5
# # for i in a:
# #     yield b
# #     print(i)
class Bird:
    # classmethod修饰的方法是类方法
    @classmethod
    def fly (cls):
        print('类方法fly: ', cls)
    # staticmethod修饰的方法是静态方法
    @staticmethod
    def info (p):
        print('静态方法info: ', p)
# # 调用类方法，Bird类会自动绑定到第一个参数
# Bird.fly()  #①
# # 调用静态方法，不会自动绑定，因此程序必须手动绑定第一个参数
# Bird.info('crazyit')
# # 创建Bird对象
# b = Bird()
# # 使用对象调用fly()类方法，其实依然还是使用类调用，
# # 因此第一个参数依然被自动绑定到Bird类
# b.fly()  #②
# # 使用对象调用info()静态方法，其实依然还是使用类调用，
# # 因此程序必须为第一个参数执行绑定
# b.info('fkit')


# !/usr/bin/python
# -*- coding: UTF-8 -*-

class A():
    bar = 1

    @staticmethod
    def func1():
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        # cls().func1()  # 调用 foo 方法
    def fun3(self):
        print('func3')

A.func1()
A.func2()  # 不需要实例化



# test = A()
# # test.func1()
# test.func2()
#

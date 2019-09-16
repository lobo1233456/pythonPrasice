import time
#
from selenium.common.exceptions import NoSuchElementException
#
#
# def foo():
#     print( 'in foo()' )
#
#
# def timeit(func):
#
#     start = time.clock()
#     func()
#     end =time.clock()
#     print ('Time Elapsed:', end - start )
#
#
#
# def makebold(func):
#     def wrapped():
#         start = time.clock()
#         func()
#         end = time.clock()
#         print('Time Elapsed:', end - start)
#         return 'Time Elapsed:', end - start
#
#     return wrapped
# # @makebold
# # class test():
#
# def foo():
#     time.sleep(3)
#     print( 'in foo()' )
#
# @makebold
# def too():
#     time.sleep(3)
#     # print("hello testtwo")
#     return "hello testtwo"
#
#
# foo = makebold(foo)   #可以直接写成@timeit + foo定义，python的"语法糖",即@makebold
# foo()
#
# def w1(fun):
#     def wrapper(name123):
#         print("this is the wrapper head")
#         fun(name123)
#         print("this is the wrapper end")
#     return wrapper
# '''
#     对有参函数进行修饰
#     一个参数
#     如果原函数有参数，那闭包函数必须保持参数个数一致，并且将参数传递给原方法
#     多个参数测试
# '''
# @w1
# def hello(name):
#     print("hello"+name)
#
# hello("world")
# def w2(fun):
#     def wrapper(*args,**kwargs):
#         print("this is the wrapper head")
#         fun(*args,**kwargs)
#         print("this is the wrapper end")
#     return wrapper
#
# @w2
# def hello(name,name2):
#     print("hello"+name+name2)
#
# hello("world","!!!多个参")
#
#
# '''
# 有返回值的函数
# '''
# def w3(fun):
#     def wrapper(*args,**kwargs):
#         print("this is the wrapper head")
#         temp=fun(*args,**kwargs)
#         print("this is the wrapper end")
#         return temp   #要把值传回去呀！！
#     return wrapper
#
# @w3
# def hello(name1,name2):
#     print("hello"+name1+name2)
#     return "hello  "+name1+name2
#
# result=hello('123','12334')
# print("After the wrapper,I accept %s" %result)

'''
万能修饰器，一切修饰器皆源于此
'''
def w_test(func):
    def inner(*args, **kwargs):
        for i in range(3):
            try:
                func(*args, **kwargs)
                # driver.quit()
            except NoSuchElementException as e:
                pass
            finally:
                i = i + 1

        # return ret
    return inner

@w_test
def test2(a):
    print('test2 called and value is %s ' % a)
test2('我是万能的')
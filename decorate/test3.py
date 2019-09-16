def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print ("I make decorators! And I accept arguments:", decorator_arg1, decorator_arg2)
    def my_decorator(func):
        # 这里传递参数的能力是借鉴了 closures.
        # 如果对closures感到困惑可以看看下面这个:
        # http://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
        print("I am the decorator. Somehow you passed me arguments:", decorator_arg1, decorator_arg2)
        # 不要忘了装饰器参数和函数参数!
        def wrapped(function_arg1, function_arg2) :
            print ("I am the wrapper around the decorated function.\n"
                  "I can access all the variables\n"
                  "\t- from the decorator: {0} {1}\n"
                  "\t- from the function call: {2} {3}\n"
                  "Then I can pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)
        return wrapped
    return my_decorator

@decorator_maker_with_arguments("Leonard", "Sheldon")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ("I am the decorated function and only knows about my arguments: {0}"
           " {1}".format(function_arg1, function_arg2))

decorated_function_with_arguments("Rajesh", "Howard")


def makeConstantAdder(x,y):
    constant = x
    def adder():

        return y + constant
    return adder

# f = makeConstantAdder(12)
print(makeConstantAdder(12)(3))
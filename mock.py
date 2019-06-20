# function.py
from unittest.mock import MagicMock


def add_and_multiply(x, y):
    addition = x + y
    multiple = multiply(x, y)
    return (addition, multiple)

def multiply(x, y):
    return x * y

class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    def something(self, a, b, c):
        pass

real = ProductionClass()
real.something = MagicMock()
real.method()
print(real.something.assert_called_once_with(1, 2, 3))
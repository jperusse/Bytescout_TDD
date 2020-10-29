import sys
from my_module import Test


class Calculator(object):

    """
    Calculator class
    """

    def add(self, a, b):
        return (a + b)
        

t = Test()
ans = t.testfunc(1,2)
# print(sys.path)

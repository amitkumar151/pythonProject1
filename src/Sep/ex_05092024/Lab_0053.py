# Methhod overloading
# python does not support method overloading
# in the traditional sense.

class Mathutil(object):
    def add(self, a, b):
        return a + b
    def add(self, a, b, c=0):
        return a +b + c

math = Mathutil()
print(math.add(3,5))     


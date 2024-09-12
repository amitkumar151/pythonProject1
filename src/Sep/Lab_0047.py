class Calcu():
    def __init__(self, a, b):
        self.a= a
        self.b= b
    def sum(self):
        return self.a +self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

obj_refer = Calcu(4, 6)
output =obj_refer.sum()
output1 =obj_refer.sub()
output2 =obj_refer.mul()
print(output, output1, output2)
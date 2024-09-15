class Calc:
    def __init__(self):
        print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


object_ref = Calc()
output_sum = object_ref.sum(3,5)
output_sub = object_ref.sub(3,5)
output_mul = object_ref.mul(3,5)
output_div = object_ref.div(3,5)
print(output_sum, output_sub, output_mul, output_div)

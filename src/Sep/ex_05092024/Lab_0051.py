class Shape:
    def area(self):
        print("print area of the shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(4, 5)

print(shape1.area())

shape2 = Circle(5)
print(shape2.area())


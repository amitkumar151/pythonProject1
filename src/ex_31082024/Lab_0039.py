# Special function in class , __init__()
# it will autmatically called  when you are create an object

class Dog:
    name = None


def __init__(self, name):
    print("called object is created ")
    self.name = name


def sleep(self):
    print("sleeping")


dog1 = Dog("chow")
print(dog1.name)

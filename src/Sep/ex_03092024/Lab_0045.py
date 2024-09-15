class Person():
    def __init__(self):
        self.name = input("enter the name\n ")
        self.age = input("enter the age\n ")
        self.phone = input("enter phone number\n")
        self.occupation = input("enter occupation\n")

    def display_information(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"phone is {self.phone}")
        print(f"occupation is {self.occupation}")


person1 = Person()
person1.display_information()

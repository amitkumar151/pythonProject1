class person():
    # Atribute
    name = None
    email = None
    age = None
    Address = None

    # Bhihaviour
    def walk(self):
        print(" i am walking")
    def sleep(self):
        return "sleeping"
    def eat(self, name):
        print("eating a mango")
    def talk(self):
        print("i can talk")
        return ("i can talk")


# create a object
amit = person()
amit.name = "Amit Kumar"
print(amit.name)
amit.talk()

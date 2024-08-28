def greet():
    print("Hello party")


def greet_by_name(name):
    print("hello,", name)


# greet()
# greet_by_name("Amit")

name = str(input("Enter your name\n"))
greet_by_name(name)

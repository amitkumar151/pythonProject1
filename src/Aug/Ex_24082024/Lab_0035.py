# create a program of sum of three number from user inlut

num1 = int(input("enter number1->"))
num2 = int(input("enter number2->"))
num3 = int(input("enter number3->"))


def sum_of_three_number(n1, n2, n3):
    return n1 + n2 + n3


result = sum_of_three_number(num1, num2, num3)
print(result)

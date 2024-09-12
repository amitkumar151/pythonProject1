# find max number in three number

num1 = int(input("enter the number 1->"))
num2 = int(input("enter the number 2->"))
num3 = int(input("enter the number 3->"))

if num1 > num2 and num1 > num3:
    print("number 1 is MAX ", num1)
elif num2 > num1 and num2 > num3:
    print("number2 is max", num2)
else:
    print("number3 is max", num3)

result = max(num1, num2, num3)
print(result)

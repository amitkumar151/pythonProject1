# give grade of examination with A,B,C,D,F
# 100-90
# 91-80
# 81-71
# 70-60
# 61-45
# 45-0

score = int(input("enter the Score \n->"))
if score >= 90 and score <= 100:
    print("you got A Grade A")
elif score >= 80 and score <= 89:
    print("you got a Grade B")
elif score >= 70 and score <= 79:
    print("you got a Grade c")
elif score >= 60 and score <= 69:
    print("you got a Grade D")
elif score >= 50 and score <= 59:
    print("you got a Grade D")
else:
    print("you are Fail ")

class employee:
    # attribute
    emp_id = None
    emp_Name = None
    emp_age = None
    emp_address = None


def __init__(self, id, name, age, address):
    self.id = id
    self.name = name
    self.age = age
    self.address = address


emp1 = employee()

emp1.emp_Name="dhiraj kumar"
print("employee name-> " +emp1.emp_Name)
emp1.emp_id=7867
print("employee id->", +emp1.emp_id)
emp1.emp_age=28
print("employee id->", emp1.emp_age)
emp1.emp_address="jariti nagar patna bihar"
print("employee address-> " +emp1.emp_address)

print("===========================")
emp2 = employee()

emp2.emp_Name="Ratnesh kumar"
print("employee name-> " +emp2.emp_Name)
emp2.emp_id=780092
print("employee id->", +emp2.emp_id)
emp2.emp_age=209
print("employee id->", emp2.emp_age)
emp2.emp_address="jariti nagar,Khjpura, patna bihar"
print("employee address-> " +emp2.emp_address)
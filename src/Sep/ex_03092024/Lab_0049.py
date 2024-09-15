class Father:
    key="3 bhk"
    def home(self):
        print("3 BHK")
    def Car(self):
        print("alto")
class Son(Father):
    def truck(self):
        print("son have truck")
father_obj= Father()
father_obj.home()
father_obj.Car()
son_obj= Son()
son_obj.key
son_obj.Car()
son_obj.truck()
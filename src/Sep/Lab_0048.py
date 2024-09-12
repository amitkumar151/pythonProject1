class Car:
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("starting a car with the name " + self.name)
        print("starting a car with the make " + self.make)
        print("starting a car with the model" + self.model)

lambo = Car(o_name="lambo", o_make="v2", o_model="2026")
lambo.start_engine()

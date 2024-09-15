from abc import ABC, abstractmethod

class PyATB(ABC):
    @abstractmethod
    def payfee(self):
        pass
    def enrolled(self):
        print("Enrolled")

class Amit(PyATB):
    def payfee(self):
        print("Paid")

tanu = Amit()
tanu.enrolled()
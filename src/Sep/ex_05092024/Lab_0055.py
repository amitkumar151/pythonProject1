from abc import ABC, abstractmethod


class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass


class Amit(Father):
    def loan(self):
        print(" paid 1 L loan")


amit = Amit("1 L")
amit.loan()

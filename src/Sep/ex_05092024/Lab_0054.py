# abstraction

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def Sound(self):
        pass
class Dog():
    def sound(self):
        print("Bark")

dog = Dog()
dog.sound()

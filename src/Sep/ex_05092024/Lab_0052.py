# method overriding --same name in the parent and child
# child always override te parent function
# super means call my parent function

class Father:
    def home(self):
        print(" 1 BHK ")

class Son(Father):
    def home(self):
        super().home()
        print(" No House")

promod = Son()
promod.home()
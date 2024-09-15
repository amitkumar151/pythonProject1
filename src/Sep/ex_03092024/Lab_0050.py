# Multilevel inhartance
class Grandfather:
    gold = "22 kg"

    def bhk1(self):
        print("1 bhk home of grandfather")


class Father(Grandfather):
    diamond = "22 karat father"

    def bhk2(self):
        print("father have 2 BHK flaat")

    def car(self):
        print("father have one BMW car")


class Son(Father):
    btc = "1 btc"

    def bhk3(self):
        print("son have 3 BHK flat")


s = Son()
s.bhk3() #in multilevel inhartiance son have taken father and grandfather attribute and bhiaviour
f = Father()
f.car()
print(f.diamond)
gf = Grandfather()
gf.bhk1()


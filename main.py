#objętość i pole powierzchni
class Sphere:
    def __init__(self, r):
        self.r = r
        self.__pi = 3.1415

    def count(self):
        print(f"Pole powierzchni: {4 * self.__pi * self.r}")
        print(f"Objętość: {4/3 * self.__pi * (self.r * self.r * self.r)}")


#obwód i pole
class Circe:
    def __init__(self, r):
        self.r = r
        self.__pi = 3.1415

    def count(self):
        print(f"Obwód: {2 * self.__pi * self.r}")
        print(f"Pole: {self.__pi * self.r * self.r}")

kolo1 = Circe(3)
kula1 = Sphere(3)
kolo1.count()
kula1.count()
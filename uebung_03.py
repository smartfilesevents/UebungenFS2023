import math

class Figur:
    def __init__(self, name):
        self.name = "Figur"

        def Umfang(self):
            return 0
        
        def __str__(self):
            return self.name

class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

class Dreieck(Figur):
    def __init__(self,ecke1,ecke2,ecke3):
         super().__init__("Dreieck")
         self.ecke1 = ecke1
         self.ecke2 = ecke2
         self.ecke3 = ecke3

    def __str__(self):
        return f"Dreieck {self.ecke1}{self.ecke2}{self.ecke3}"

    def umfang(self):
        return (((self.ecke1.x-self.ecke2.x)**2+(self.ecke1.y-self.ecke2.y)**2)**0.5+
                ((self.ecke2.x-self.ecke3.x)**2+(self.ecke2.y-self.ecke3.y)**2)**0.5+
                ((self.ecke3.x-self.ecke1.x)**2+(self.ecke3.y-self.ecke1.y)**2)**0.5)


class Rechteck(Figur):
    def __init__(self,ecke1,ecke2):
        self.ecke1 = ecke1
        self.ecke2 = ecke2
        super().__init__("Rechteck")

    def __str__(self):
        return f"Rechteck {self.ecke1}{self.ecke2}"
    
    def umfang(self):
        return (abs(self.ecke1.x-self.ecke2.x)*2+
                abs(self.ecke1.y-self.ecke2.y)*2)


class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def umfang(self):
        return self.radius*2*math.pi
    
    def __str__(self):
        return f"Kries M = {self.mittelpunkt} r={self.radius}"
    

## Funktioniert leider noch nicht...
class Polygon(Figur):
    def __init__(self, *ecke):
        if len(ecke) == 1 and isinstance(ecke[0], (list, tuple)):
            self.ecke = ecke[0]
        else:
            self.ecke = ecke
        super().__init__("Polygon")
    
    def __str__(self):
        return f"Polygon {self.ecke}"






P1 = Punkt(2,3)
P2 = Punkt(3,4)
P3 = Punkt(1,1)

k1 = Kreis(P1,10)

print(k1)
print(k1.umfang())

d1 = Dreieck(P1,P2,P3)
print(d1)
print(d1.umfang())

r1 = Rechteck(P1,P2)
print(r1)
print(r1.umfang())

p1 = Polygon(P1,P2,P3)
print(p1)
class Figur:
    def __init__(self, name="Figur"):
        self.name = name

    def Umfang(self):
        return 0
    
    def __str__(self):
        return self.name
    
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Kreis(Figur):
    def __init__(self, zentrum, radius):
        super().__init__("Kreis")
        self.zentrum = zentrum
        self.radius = radius

    def Umfang(self):
        return 2 * 3.14159 * self.radius
    
    def __str__(self):
        return f"{self.name} M= ({self.zentrum.x}, {self.zentrum.y}), r= {self.radius}"

k = Kreis(Punkt(2, 3), 4)
print(k.Umfang())
print(k)

class Dreieck(Figur):
    def __init__(self, d1, d2, d3):
        super().__init__("Dreieck")
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

    def Umfang(self):
        a = ((self.d2.x - self.d1.x)**2 + (self.d2.y - self.d1.y)**2)**0.5
        b = ((self.d3.x - self.d2.x)**2 + (self.d3.y - self.d2.y)**2)**0.5
        c = ((self.d1.x - self.d3.x)**2 + (self.d1.y - self.d3.y)**2)**0.5
        return a + b + c
    
    def __str__(self):
        return f"{self.name} ({self.d1.x}, {self.d1.y}) - ({self.d2.x}, {self.d2.y}) - ({self.d3.x}, {self.d3.y})"

d = Dreieck(Punkt(1, 1), Punkt(3, 1), Punkt(2, 3))
print(d.Umfang())
print(d)

class Rechteck(Figur):
    def __init__(self, r1, r2):
        super().__init__("Rechteck")
        self.r1 = r1
        self.r2 = r2

    def Umfang(self):
        a = abs(self.r2.x - self.r1.x)
        b = abs(self.r2.y - self.r1.y)
        return 2 * a + 2 * b
    
    def __str__(self):
        return f"{self.name} ({self.r1.x}, {self.r1.y}) - ({self.r2.x}, {self.r2.y})"

r = Rechteck(Punkt(1, 1), Punkt(3, 3))
print(r.Umfang())
print(r)

class Polygon(Figur):
    def __init__(self, points):
        super().__init__("Polygon")
        self.points = points

    def Umfang(self):
        u = 0
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % len(self.points)]
            u += ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5
        return u
    
    def __str__(self):
        s = f"{self.name} "
        for p in self.points:
            s += f"({p.x}, {p.y}) - "
        return s[:-3]

p = Polygon([Punkt(1, 1), Punkt(3, 1), Punkt(3, 3)])
print(p.Umfang())
print(p)

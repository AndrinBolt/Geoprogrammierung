#Implementieren Sie eine Klasse Vector3, welche einen 3D Vektor repräsentiert.
#Dabei sollen Magische Methoden implementiert werden:
#• Konversion zu Zeichenkette
#• Addition
#• Subtraktion
#• komponentenweise Multiplikation (Vector3 * Vector3)
#• Multiplikation mit Skalar 
#(float * Vector3) oder (int * Vector3) oder
#(Vector3 * float) oder (Vector3 * int)
#a = Vector3(3,4,2)
#b = Vector3(2,1,0)
#c = a * b # Komponentenweise Multiplikation
#print(c)
#d = a.dot(b) # Skalarprodukt
#e = a.cross(b) # Kreuzprodukt
#Implementieren sie zudem auch folgende Methoden
#cross(b) Berechnung des Kreuzproduktes
#dot(b) Berechnung des Skalarprodukes
#normalize() Vektor normalisieren
#zur Erinnerung: 
#• https://de.wikipedia.org/wiki/Kreuzprodukt
#• https://de.wikipedia.org/wiki/Skalarprodukt
#Hinweis / Repetition: Datentypen können folgendermassen überprüft werden:
#a = 12.5
# a = 5
# a = Vector3(23,4,2)
#if type(a) == Vector3:
#print("a ist eine Vektor3-Klasse")
#if type(a) == float:
#print("a ist ein float")
#if type(a) == int:
#print("a ist ein Integer")

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setZ(self, z):
        self.z = z

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    x = property(getX, setX)
    y = property(getY, setY)
    z = property(getZ, setZ)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}"

    def __add__(self, addVector):
        return Vector3(self.x + addVector.x, self.y + addVector.y, self.z + addVector.z)

    def __sub__(self, subVector):
        return Vector3(self.x - subVector.x, self.y - subVector.y, self.z - subVector.z)

    def __mul__(self, mulVector):
        try:
            return Vector3(self.x * mulVector.x, self.y * mulVector.y, self.z * mulVector.z)
        except AttributeError:
            return Vector3(self.x * mulVector, self.y * mulVector, self.z * mulVector)

    def __rmul__(self, mulVector):
        return self.__mul__(mulVector)

    def len(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def dot(self, mulVector):
        return self.x * mulVector.x + self.y * mulVector.y + self.z * mulVector.z

    def cross(self, mulVector):
        return Vector3(
            self.y * mulVector.z - self.z * mulVector.y,
            self.z * mulVector.x - self.x * mulVector.z,
            self.x * mulVector.y - self.y * mulVector.x
        )

    def normalize(self):
        länge = self.len()
        if länge == 0:
            return Vector3(0, 0, 0)
        return Vector3(self.x / länge, self.y / länge, self.z / länge)

a = Vector3(3, 4, 2)
b = Vector3(2, 1, 0)

c = a + b
print(c)  # Ausgabe: x: 5, y: 5, z: 2

d = a - b
print(d)  # Ausgabe: x: 1, y: 3, z: 2

e = a * b
print(e)  # Ausgabe: x: 6, y: 4, z: 0

f = a * 2
print(f)  # Ausgabe: x: 6, y: 8, z: 4

g = a.dot(b)
print(g)  # Ausgabe: 14

h = a.cross(b)
print(h)  # Ausgabe: x: -2, y: 4, z: -2

i = a.normalize()
print(i)  # Ausgabe: x: 0.6, y: 0.8, z: 0.4

# Testen der setX-Methode
a = Vector3(3, 4, 2)
print(f"Vor dem Setzen: {a}")  # Ausgabe: x: 3, y: 4, z: 2

a.setX(10)
print(f"Nach dem Setzen: {a}")  # Ausgabe: x: 10, y: 4, z: 2
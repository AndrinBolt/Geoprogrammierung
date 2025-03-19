#Erstellen Sie eine Klasse Vector3, welche einen dreidimensionalen Vektor
#repräsentiert.
#Über den Konstruktor werden die Komponenten x, y und z definiert. Wird nichts
#angegeben, so wird ein Null-Vektor erstellt.
#Entwickeln Sie eine Methode len, welche die Länge des Vektors berechnet.
#Mit einer Instanz von Vector3 soll die Klasse getestet werden.

class Vector3():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
v = Vector3(5, 3, 9)
print(v.len())

    #def setX(self,x):
    #    return self.x
    #def setY(self,y):
    #    return self.y
    #def setZ(self,z):
    #    return self.z
    #def getX(self):
    #    return self.x
    #def getY(self):
    #    return self.y
    #def getZ(self):
    #    return self.z

    #def __str__(self):
        #return f"x: {self.x}, y:{self.y}, z:{self.z}"

    #def __add__(self, addVector):
        #return Vector3(self.x + addVector.x, self.y + addVector.y, self.z + addVector.z)

    #def addition(self, addVector):
        #return Vector3(self.x + addVector.x, self.y + addVector.y, self.z + addVector.z)

    #x=property(getX, setX)
    #y=property(getY, setY)
    #z=property(getZ, setZ)

#v0=Vector3(1,2,1)
#v1=Vector3(2,0,0)

#v2=v0+v1
#v2=v0.addition(v1)

#print(v2)

#class Plane:
#    def __init__(self, v0,v1):
#        self.v0=v0
#        self.v1=v1

#    def setV0(self,v0):
#        self.v0=v0

#    def getV0(self):
#        return self.v0

#    def setV1(self,v1):
#        self.v1=v1

#    def getV1(self):
#        return self.v1

#    v0=property(getV0, setV0)
#    v1=property(getV1, setV1)

#v0=Vector(1,0,0)
#v1=Vector(0,1,0)

#p0=Plane(v0,v1)

#print(p0.v0)
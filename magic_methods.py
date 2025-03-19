class Temperatur:
    def __init__(self, temperatur):
        self._temperatur = temperatur

    def setTemperatur(self, temperatur):
        self._temperatur = temperatur

    def getTemperatur(self):
        return self._temperatur
    
    def __str__(self): #toString
        return f"Celsius: {self._temperatur}"
    
    def __int__ (self): #toInt
        return 1
    
    def __float__ (self): #toFloat
        return float(self._temperatur)
    
    def __add__(self, addValue): #add
        return Temperatur(self._temperatur + float(addValue))
    
    def __gt__(self, compareValue):
        return float(self) > float(compareValue)
    
    def __lt__(self, compareValue):
        return True
    
    temperatur = property(getTemperatur, setTemperatur)

t0=Temperatur(150)
t1=Temperatur(100)

print(t0>t1)
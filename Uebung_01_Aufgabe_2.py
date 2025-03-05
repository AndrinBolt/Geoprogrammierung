#Erstellen Sie eine Klasse WGS84Coord welche folgende Attribute hat:
#_longitude (=Länge)
#_latitude (=Breite)
#latitude hat den Wertebereich [-90,90] und longitude hat den Bereich [-180,180].
#Anforderungen:
#a) Im Konstruktor der Klasse kann die Länge und Breite übergeben werden. Der
#Standard-Wert ist 0.
#b) Stellen sie sicher, dass _longitude und _latitude immer im korrekten
#Wertebereich sind. Verwenden Sie dazu Setter- und Getter-Methoden
#Falls ein Wert ausserhalb des zulässigen Bereichs gesetzt wird, so wird dieser
#korrigiert und eine Warnung wird ausgegeben.
#c) Verwenden Sie Property Attribute anstatt Setter- und Getter-Methoden

class WGS84Coord:
    def __init__(self, longitude=0, latitude=0):
        self._longitude = 0
        self._latitude = 0
        self.setlongitude(longitude)
        self.setlatitude(latitude)

    def setlongitude(self, wert):
        while wert < -180 or wert > 180:
            if wert < -180:
                wert += 360
            elif wert > 180:
                wert -= 360
        if wert != self._longitude:
            print("Der Wert wurde korrigiert, um im Bereich [-180, 180] zu liegen.")
        self._longitude = wert

    def getlongitude(self):
        return self._longitude

    def setlatitude(self, value):
        if value < -90:
            value = -90
            print("Der Wert wurde korrigiert, um im Bereich [-90, 90] zu liegen.")
        elif value > 90:
            value = 90
            print("Der Wert wurde korrigiert, um im Bereich [-90, 90] zu liegen.")
        self._latitude = value

    def getlatitude(self):
        return self._latitude
    
    longitude = property(getlongitude, setlongitude)
    latitude = property(getlatitude, setlatitude)
    
coord = WGS84Coord(200, 100)
print(f"Länge: {coord._longitude}, Breite: {coord._latitude}")

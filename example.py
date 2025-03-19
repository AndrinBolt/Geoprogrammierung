value1=50
value1+=10
print(value1)

# += entspricht

def __add__(self, addValue): #add
    self._temperatur += float(addValue)
    return self

#wird zu

def __iadd__(self, addValue): #add
    self._temperatur += float(addValue)
    return self


def __mul__(self, multiplication):
    self._temperatur *= multiplication
    return self

#umgekerter Vektor = *-1


import math

def compara(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1
    
def ipotenusa(cateto1, cateto2):
    quadrato1 = cateto1**2
    quadrato2 = cateto2**2
    return round(math.sqrt(quadrato1 + quadrato2), 2)

def compreso_tra(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False
    
def fattoriale(n):
    if not isinstance(n, int):
        print('Il fattoriale è definito solo per numeri interi.')
        return None
    elif n < 0:
        print('Il fattoriale non è definito per interi negativi.')
        return None
    elif n == 0:
        return 1
    else:
        return n * fattoriale(n - 1) # type: ignore

def divisibile(x, y):
    if x % y == 0:
        return True
    else:
        return False
    
def potenza(a, b):
    if a == b:
        return True
    elif divisibile(a, b):
        return potenza(a/b, b)
    else:
        return False
    
def length(lista):
    n = 0
    while lista != []:
        del lista[0]
        n += 1
    return n
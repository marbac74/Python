import math

class Punto:
    """ Rappresenta un punto su un piano cartesiano
    attributi: x, y
    """

class Rettangolo:
    """ Rappresenta un rettangolo
    attributi: larghezza, altezza, angolo
    """

def stampa_punto(punto):
    print('(%g, %g)' % (punto.x, punto.y))

def distanza_tra_punti(punto1, punto2):

    quadrato_diff_x = (punto2.x - punto1.x)**2
    quadrato_diff_y = (punto2.y - punto1.y)**2 

    return math.sqrt(quadrato_diff_x + quadrato_diff_y)

def trova_centro(rettangolo):
    p = Punto()
    p.x = rettangolo.angolo.x + rettangolo.larghezza/2 # type: ignore
    p.y = rettangolo.angolo.y + rettangolo.altezza/2 # type: ignore
    return p

def modifica_rettangolo(rettangolo, delta_lar, delta_alt):
    rettangolo.larghezza += delta_lar
    rettangolo.altezza += delta_alt

def sposta_rettangolo(rett, dx, dy):
    rett.angolo.x += dx
    rett.angolo.y += dy
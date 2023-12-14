import math
import copy
import turtle

class Punto:
    """ Rappresenta un punto su un piano cartesiano
    attributi: x, y
    """

class Rettangolo:
    """ Rappresenta un rettangolo
    attributi: larghezza, altezza, angolo
    """

class Cerchio:
    """ Rappresenta un cerchio
    attributi: centro, raggio
    """
class Tempo:
    """ Rappresenta un'ora del giorno
    attributi: ore, minuti, secondi
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

def sposta_copia_rettangolo(rett, dx, dy):
    copia_rett = copy.deepcopy(rett)
    copia_rett.angolo.x += dx
    copia_rett.angolo.y += dy

def stampa_tempo(tempo):
    print('%.2d:%.2d:%.2d' % (tempo.ore, tempo.minuti, tempo.secondi))

def viene_dopo(t1, t2):
    temp_val1 = (t1.ore * 3600) + (t1.minuti * 60) + t1.secondi
    temp_val2 = (t2.ore * 3600) + (t2.minuti * 60) + t2.secondi
    if temp_val1 > temp_val2:
        return True
    else:
        return False

def somma_tempo(t1, t2):
    somma = Tempo()
    somma.ore = t1.ore + t2.ore # type: ignore
    somma.minuti = t1.minuti + t2.minuti  # type: ignore
    somma.secondi = t1.secondi + t2.secondi  # type: ignore

    if somma.secondi >= 60: # type: ignore
        somma.secondi -= 60 # type: ignore
        somma.minuti += 1 # type: ignore

    if somma.minuti >= 60: # type: ignore
        somma.minuti -= 60 # type: ignore
        somma.ore += 1 # type: ignore

    return somma

def incremento(tempo, secondi):
    
    tempo.secondi += secondi

    if tempo.secondi >= 60:
        minuti_in_più = tempo.secondi // 60
        nuovi_secondi = tempo.secondi % 60
        tempo.secondi = nuovi_secondi
        tempo.minuti += minuti_in_più

    if tempo.minuti >= 60:
        ore_in_più = tempo.minuti // 60
        nuovi_minuti = tempo.minuti % 60
        tempo.minuti = nuovi_minuti
        tempo.ore += ore_in_più

def puroincremento(tempo, secondi):
    
    incremento = Tempo()
    incremento = copy.copy(tempo)

    incremento.secondi += secondi

    if incremento.secondi >= 60:
        minuti_in_più = incremento.secondi // 60
        nuovi_secondi = incremento.secondi % 60
        incremento.secondi = nuovi_secondi
        incremento.minuti += minuti_in_più

    if incremento.minuti >= 60:
        ore_in_più = incremento.minuti // 60
        nuovi_minuti = incremento.minuti % 60
        incremento.minuti = nuovi_minuti
        incremento.ore += ore_in_più
    
    return incremento

box = Rettangolo()
box.larghezza = 100.0 # type: ignore
box.altezza = 200.0 # type: ignore
box.angolo = Punto() # type: ignore
box.angolo.x = 50.0 # type: ignore
box.angolo.y = 50.0 # type: ignore

"""
circle = Cerchio()
circle.centro = Punto() # type: ignore
circle.centro.x = 150.0 # type: ignore
circle.centro.y = 100.0 # type: ignore
circle.raggio = 75.0 # type: ignore
"""

def punto_nel_cerchio(cerchio, punto):
    centro = cerchio.centro
    distanza = distanza_tra_punti(centro, punto)
    if distanza <= cerchio.raggio:
        return True
    else:
        return False

def rett_nel_cerchio(cerchio, rettangolo):
    angolo = rettangolo.angolo
    if not punto_nel_cerchio(cerchio, angolo):
        return False
    angolo.y += rettangolo.altezza
    if not punto_nel_cerchio(cerchio, angolo):
        return False
    angolo.x += rettangolo.larghezza
    if not punto_nel_cerchio(cerchio, angolo):
        return False
    angolo.y -= rettangolo.altezza
    if not punto_nel_cerchio(cerchio, angolo):
        return False
    return True

def rett_cerchio_sovrapp(cerchio, rettangolo):
    angolo = rettangolo.angolo
    if punto_nel_cerchio(cerchio, angolo):
        return True
    angolo.y += rettangolo.altezza
    if punto_nel_cerchio(cerchio, angolo):
        return True
    angolo.x += rettangolo.larghezza
    if punto_nel_cerchio(cerchio, angolo):
        return True
    angolo.y -= rettangolo.altezza
    if punto_nel_cerchio(cerchio, angolo):
        return True
    return False

def disegna_rett(tarta, rett):
    
    # disegna il rettangolo
    tarta.pu()
    a = rett.angolo.x
    print(a)
    b = rett.angolo.y
    print(b)
    tarta.goto(a, b)
    tarta.setheading(0)
    tarta.pd()
    tarta.fd(rett.larghezza)
    tarta.lt(90)
    tarta.fd(rett.altezza)
    tarta.lt(90)
    tarta.fd(rett.larghezza)
    tarta.lt(90)
    tarta.fd(rett.altezza)
    tarta.lt(90)
    turtle.mainloop()

def main():
    pen = turtle.Turtle()
    # print(punto_nel_cerchio(circle, box.angolo)) # type: ignore
    # print(rett_nel_cerchio(circle, box))
    # print(rett_cerchio_sovrapp(circle, box))
    # disegna gli assi
    length = 400
    pen.fd(length)
    pen.bk(length)
    pen.lt(90)
    pen.fd(length)
    pen.bk(length)
    pen.rt(90)
    disegna_rett(pen, box)


if __name__ == '__main__':
    main()
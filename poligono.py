import turtle
import math

bob = turtle.Turtle()

turtle.bgcolor('orange')

def poligono(turtle, num_lati, lunghezza, d_s, a_d):
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    angolo = 360 / num_lati
    polilinea(turtle, num_lati, lunghezza, angolo, d_s, a_d)
    turtle.end_fill()

def polilinea(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arco(turtle, raggio, angolo):
    arco_lunghezza = 2 * math.pi * raggio * angolo / 360
    n = int(arco_lunghezza / 3) + 1
    passo_lunghezza = arco_lunghezza / n
    passo_angolo = float(angolo) / n
    polilinea(turtle, n, passo_lunghezza, passo_angolo)

def cerchio(t, r):
    arco(t, r, 360)



turtle.mainloop()

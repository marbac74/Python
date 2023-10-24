import turtle
import math

torta = turtle.Turtle()


def draw_pie(tartaruga, lato, numero_triangoli):
    tartaruga.speed(2)
    tartaruga.pensize(2)
    angolo_vertice = 360 / numero_triangoli
    angolo_base = (180 - angolo_vertice) / 2
    base = 2*lato*math.cos(math.radians(angolo_base))
    for i in range(numero_triangoli):
        draw_triangle(tartaruga, lato, base, angolo_base)

def draw_triangle(tartaruga, lato, base, angolo_base):
    tartaruga.fd(lato)
    tartaruga.lt(180 - angolo_base)
    tartaruga.fd(base)
    tartaruga.lt(180 - angolo_base)
    tartaruga.fd(lato)
    tartaruga.seth(tartaruga.heading() - 180)

turtle.bgcolor('black')

torta.pu()
torta.goto(-200, 0)
torta.pd()
torta.pencolor('red')
draw_pie(torta, 100, 5)

torta.pu()
torta.goto(0, 0)
torta.pd()
torta.pencolor('yellow')
draw_pie(torta, 100, 6)

torta.pu()
torta.goto(192, 0)
torta.pd()
torta.pencolor('orange')
draw_pie(torta, 100, 7)


turtle.mainloop()
    

import turtle

a_turtle = turtle.Turtle()

def koch(t, l):
    if l < 3:
        t.fd(l)
    else:
        koch(t, l/3)
        t.lt(60)
        koch(t, l/3)
        t.rt(120)
        koch(t, l/3)
        t.lt(60)
        koch(t, l/3)

def fioccodineve(t, n):
    """Disegna un fiocco di neve (un triangolo con una curva di Koch
       per ogni lato)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


koch(a_turtle, 200)
turtle.resetscreen()
fioccodineve(a_turtle, 180)

turtle.mainloop()

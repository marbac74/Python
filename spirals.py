import turtle

my_turtle = turtle.Turtle()
colori = ['red', 'indigo', 'darkgreen', 'grey', 'pink',
          'blue', 'yellow', 'orange', 'brown']

def drawline(turtle, start, stop):
    for step in range(start, stop, 20):
        turtle.fd(step)
        turtle.lt(90)
        turtle.fd(step)
        turtle.lt(90)

def drawrev(turtle, start, stop):
    for step in range(start, stop, -20):
        turtle.fd(step)
        turtle.rt(90)
        turtle.fd(step)
        turtle.rt(90)
    

def draw_spiral(turtle, max_step, angle, colors_list):
    for step in range(max_step):
        for c in colors_list:
            turtle.color(c)
            turtle.fd(step)
            turtle.lt(angle)

def draw_spiral_1(turtle, max_radius):
    index = 0
    for step in range(max_radius, 10, -10):
        turtle.fillcolor(colori[index])
        turtle.begin_fill()
        turtle.seth(0)
        turtle.circle(step)
        turtle.seth(180)
        turtle.circle(step)
        turtle.end_fill()
        index = index + 1
        
# draw_spiral_1(my_turtle, 100)

def draw_s(t):
    start = t.pos()
    t.circle(30, 180)
    pos = t.pos()
    t.pu()
    t.goto(round(pos[0], 3), round(pos[1], 3) + 60)
    t.pd()
    t.circle(30, 180)
    t.pu()
    t.goto(start)
    t.pd()

def move_up(t):
    start = t.pos()
    t.pu()
    t.goto(round(start[0], 3), round(start[1], 3) + 30)
    t.pd()

drawline(my_turtle, 20, 200)
my_turtle.fd(180)
my_turtle.rt(90)
drawrev(my_turtle, 180, 0)

"""
for i in range(7):
    my_turtle.pencolor(colori[i])
    my_turtle.width(2)
    draw_s(my_turtle)
    move_up(my_turtle)




turtle.bgcolor('grey')
draw_spiral(my_turtle, 100, 30, ['darkblue', 'lightblue'])
turtle.resetscreen()
turtle.bgcolor('black')
draw_spiral(my_turtle, 100, 50, ['red', 'orange', 'yellow'])
"""

turtle.mainloop()

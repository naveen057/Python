import turtle
n=turtle.Turtle()
n.getscreen().bgcolor("cyan")
n.color("red","yellow")
n.pensize(1.5)
n.begin_fill()
n.speed(25)
for i in range(1,100) :
    n.fd(250)
    n.lt(155)
    

n.end_fill()
n.hideturtle()
n.Done()
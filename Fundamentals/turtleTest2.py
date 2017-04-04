import turtle
screen = turtle.Screen()
turtle.listen(xdummy=None, ydummy=None)
def f():
     turtle.fd(5)
def l():
    turtle.lt(10)
def r():
    turtle.rt(9)
def togglePen():
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()

screen.onkey(f, "Up")
screen.onkey(l, "Left")
screen.onkey(togglePen, "Down")
screen.onkey(r, "Right")
screen.listen()
turtle.done()
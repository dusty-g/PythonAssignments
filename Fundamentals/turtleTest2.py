import turtle


# this is import but I don't understand why
screen = turtle.Screen()
turtle.listen(xdummy=None, ydummy=None)

# define turtle functions
def f():
    # move forward 5 pixels
     turtle.fd(5)
def l():
    # rotate left 10 degrees
    turtle.lt(10)
def r():
    # rotate right 9 degrees
    turtle.rt(9)
def togglePen():
    # if the pen is "down", penup()
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()

# onkey(function, key)
screen.onkey(f, "Up")
screen.onkey(l, "Left")
screen.onkey(togglePen, "Down")
screen.onkey(r, "Right")
screen.listen()
turtle.done()
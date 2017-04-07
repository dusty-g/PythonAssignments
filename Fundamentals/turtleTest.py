
import turtle

# the distance we want the pointer to travel each time
count = 1
turtle.shape("turtle")
turtle.speed(10)
while count < 500:
    # if count % 2 == 0:
    #     turtle.penup()
    # else:
    #     turtle.pendown()

    
    turtle.forward(count)
    turtle.right(90)
    count += 1
turtle.done()
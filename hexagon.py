import turtle

def hexagon():
    for i in range(6):
        turtle.forward(100)
        turtle.left(60)

hexagon()

def vypln():
    for i in range(3):
        turtle.left(60)
        turtle.forward(200)
        turtle.penup()
        turtle.left(120)
        turtle.forward(100)
        turtle.left(60)
        turtle.pendown()
        

vypln()
input("")
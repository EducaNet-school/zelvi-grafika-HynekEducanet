import turtle

sides = 10
length = 100

def polygon():
    for i in range (sides):
        turtle.forward(length)
        turtle.right(360 / sides)

polygon()
input("")
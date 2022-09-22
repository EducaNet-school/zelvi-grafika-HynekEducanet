import turtle

def spiral():
    for i in range(10 * 4):
        turtle.forward(i * 10)
        turtle.right(90)

spiral()
input("")
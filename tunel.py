import turtle
size = 100
def tunel(size):
   for i in range(4):
       turtle.forward(size)
       turtle.left(90)
sizevar = 1
for i in range(10):
   tunel(sizevar)
   sizevar += 20
   turtle.penup()
   turtle.backward(10)
   turtle.right(90)
   turtle.forward(10)
   turtle.left(90)
   turtle.pendown()

input("")
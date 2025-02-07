import turtle 
from tkinter import *

button = turtle.Turtle()

test = turtle.Turtle()
test.speed(10)
turtle.title("Fibonacci Sequence Project")
def shape(numsides,size):
    for i in range(numsides):
        test.forward(size)
        test.left(360/numsides)

def fibonacci_circle(maximum):
    test.teleport(0, -500)
    last = [1,1]
    test.pendown()
    for i in range(1,maximum+1):
        last.append(last[i] + last[i-1])
        test.circle(last[i])
        print(last[i])

def fibonacci_shape(numsides, maximum):
    test.teleport(-750, -500)
    last = [1,1]
    test.pendown()
    for i in range(1, maximum+1):
        last.append(last[i] + last[i-1])
        shape(numsides, last[i])
        print(last[i])
fibonacci_shape(5,17)
turtle.done()





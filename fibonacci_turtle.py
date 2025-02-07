import turtle
from tkinter import *
from time import sleep


turtle.ht()
end = turtle.Turtle(visible=False)
turtle.register_shape('quit.gif')
end.shape('quit.gif')
end.teleport(-500,-575)
end.st()

home = turtle.Turtle(visible=False)
turtle.register_shape('home.gif')
home.shape('home.gif')
home.teleport(470, -575)
button_circle = turtle.Turtle(visible=False)
turtle.register_shape('circle.gif')
button_circle.shape('circle.gif')
button_circle.teleport(-300, 100)
button_circle.st()

writer = turtle.Turtle(visible=False)

shaper = turtle.Turtle(visible=False)
shaper.speed(11)
shaper.ht()
turtle.title("Fibonacci Sequence Project")


def start(x,y):
    turtle.clear()
    shaper.clear()
    writer.teleport(0, 600)
    writer.write("Welcome! What would you like to draw?",False, CENTER, ("Oswald", 30, "bold"))
    button_circle.st()

def shape(numsides,size):
    for i in range(numsides):
        shaper.forward(size)
        shaper.left(360/numsides)

def fibonacci_circle(x,y):
    home.ht()
    end.ht()
    writer.clear()
    button_circle.ht()
    shaper.teleport(0, -500)
    shaper.st()
    last = [1,1]
    shaper.pendown()
    for i in range(1,17):
        last.append(last[i] + last[i-1])
        shaper.circle(last[i])
        print(last[i])
    end.st()
    home.st()
    shaper.ht()

def fibonacci_shape(numsides, maximum):
    shaper.teleport(-750, -500)
    shaper.st()
    last = [1,1]
    shaper.pendown()
    for i in range(1, maximum+1):
        last.append(last[i] + last[i-1])
        shape(numsides, last[i])
        print(last[i])

def exit(x, y):
    quit()

start(0,0)


end.onclick(exit)
button_circle.onclick(fibonacci_circle)
home.onclick(start)
turtle.done()

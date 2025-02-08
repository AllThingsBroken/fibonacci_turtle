import turtle
from tkinter import *
from time import sleep


sides = 3
quit_confirm = False


turtle.ht()
end = turtle.Turtle(visible=False)
turtle.register_shape('quit.gif')
end.shape('quit.gif')
end.teleport(0,-575)
end.st()
home = turtle.Turtle(visible=False)
turtle.register_shape('home.gif')
home.shape('home.gif')
home.teleport(-470, -575)


button_circle = turtle.Turtle(visible=False)
turtle.register_shape('circle.gif')
button_circle.shape('circle.gif')
button_circle.teleport(-300, 125)
button_circle.st()

button_other = turtle.Turtle(visible=False)
turtle.register_shape('other_shape.gif')
button_other.shape('other_shape.gif')
button_other.teleport(300,140)

button_plus = turtle.Turtle(visible=False)
turtle.register_shape('plus.gif')
button_plus.shape('plus.gif')

button_minus = turtle.Turtle(visible=False)
turtle.register_shape('minus.gif')
button_minus.shape('minus.gif')

button_confirm = turtle.Turtle(visible=False)
turtle.register_shape('confirm.gif')
button_confirm.shape('confirm.gif')

button_plus.teleport(200, 148)
button_minus.teleport(-200, 150)
button_confirm.teleport(3, 35)

quit_writer = turtle.Turtle(visible=False)
quit_writer.teleport(0,-500)
writer = turtle.Turtle(visible=False)

sidecount_writer = turtle.Turtle(visible=False)
sidecount_writer.teleport(0, 120)

shaper = turtle.Turtle(visible=False)
shaper.speed(11)
shaper.ht()
turtle.title("Fibonacci Sequence Project")


def start(x,y):
    global quit_confirm
    quit_writer.clear()
    quit_confirm = False
    sidecount_writer.clear()
    turtle.clear()
    writer.clear()
    shaper.clear()
    button_minus.ht()
    button_plus.ht()
    button_confirm.ht()
    home.ht()
    end.teleport(0, -575)
    writer.teleport(0, 600)
    writer.write("Welcome! What shape would you like to experience the fibonacci sequence in?",False, CENTER, ("Oswald", 30, "bold"))
    writer.teleport(-300, 250)
    writer.write("circle", False, "center",("Oswald", 12, "bold"))
    writer.teleport(300, 250)
    writer.write("other shape", False, "center",("Oswald", 12, "bold"))
    button_circle.st()
    button_other.st()
    

def shape(numsides,size):
    for i in range(numsides):
        shaper.forward(size)
        shaper.left(360/numsides)

def fibonacci_circle(x,y):
    global quit_confirm
    quit_writer.clear()
    quit_confirm = False
    button_confirm.ht()
    home.ht()
    end.ht()
    writer.clear()
    button_other.ht()
    button_circle.ht()
    shaper.teleport(0, -500)
    last = [1,1]
    shaper.pendown()
    for i in range(1,17):
        last.append(last[i] + last[i-1])
        shaper.circle(last[i])
        print(last[i])
        sleep(0.2)
    end.teleport(470, -575)
    end.st()
    home.st()

def fibonacci_shape(x, y):
    global quit_confirm
    global sides
    quit_writer.clear()
    quit_confirm = False
    home.ht()
    end.ht()
    writer.clear()
    button_minus.ht()
    button_plus.ht()
    sidecount_writer.clear()
    button_confirm.ht()
    button_other.ht()
    button_circle.ht()
    shaper.teleport(-950, -500)
    shaper.st()
    last = [1,1]
    shaper.pendown()
    for i in range(1, 18):
        last.append(last[i] + last[i-1])
        shape(sides, last[i])
        print(last[i])
    end.teleport(470, -575)
    end.st()
    home.st()
    shaper.ht()

end.teleport(470, -575)
end.st()
home.st()
shaper.ht()

def exit(x, y):
    global quit_confirm
    if quit_confirm:
        quit()
    else:
        quit_confirm = True
        quit_writer.write("Press the quit button again to confirm",False, CENTER, ("Oswald", 12, "bold"))

def other(x, y):
    global quit_confirm
    quit_writer.clear()
    quit_confirm = False
    button_circle.ht()
    button_other.ht()
    writer.clear()
    writer.teleport(0, 600)
    writer.write("How many sides?",False, CENTER, ("Oswald", 30, "bold"))
    button_minus.st()
    button_plus.st()
    button_confirm.st()
    end.teleport(470, -575)
    home.st()
    sidecount_writer.write(sides, False, CENTER, ("Oswald", 30, "bold"))

def more_sides(x,y):
    global sides
    sides += 1
    sidecount_writer.clear()
    sidecount_writer.write(sides, False, CENTER, ("Oswald", 30, "bold"))
    print(sides)

def less_sides(x,y):
    global sides
    if sides > 3:
        sides -= 1
        sidecount_writer.clear()
        sidecount_writer.write(sides, False, CENTER, ("Oswald", 30, "bold"))
        print(sides)

start(0,0)
button_plus.onclick(more_sides)
button_minus.onclick(less_sides)
end.onclick(exit)
button_circle.onclick(fibonacci_circle)
home.onclick(start)
button_other.onclick(other)
button_confirm.onclick(fibonacci_shape)

turtle.done()

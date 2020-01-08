import turtle
import time
import random

w_width, w_hight = 800, 600

window = turtle.Screen()
window.title("Snake by Vadim")
window.bgcolor("black")
window.setup(width=w_width+35,height=w_hight+35)


# ----------- Border -----------
t0 = turtle.Turtle()
t0.speed(0)
t0.penup()
t0.pensize(10)
t0.goto(-w_width/2,-w_hight/2)
t0.pendown()
t0.color("green")
t0.hideturtle()
for i in range(2):
    t0.forward(w_width)
    t0.left(90)
    t0.forward(w_hight)
    t0.left(90)






window.mainloop()


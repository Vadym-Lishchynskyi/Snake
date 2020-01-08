import turtle
import time
import random

w_width, w_hight = 800, 600
delay = 0.1

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


# -------- Snake's Head ----------
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,100)
head.direction = "stop"


# -------- Move snake -----------
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.ycor()
        head.sety(x - 20)


while True:
    window.update()
    move()
    time.sleep(delay)


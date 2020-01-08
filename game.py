import turtle
import time
import random

w_width, w_hight = 800, 600
delay = 0.2

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
head.goto(0, 100)
head.direction = "stop"

# ------------ The array were parts of the snake's body is collected---------------
segments = []

# -------- Move snake -----------
def move():
    if len(segments) != 0:
        for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
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
        x = head.xcor()
        head.setx(x - 20)

# ---------- Changable direction -------------
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"


# ------------ keyboard bindings ------------

window.listen()
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_right, "d")
window.onkey(go_left, "a")

# ------------ Food object ----------------
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.shapesize(0.50, 0.50)

while True:
    window.update()
    move()
    time.sleep(delay)
    if head.distance(food) < 15:
        x = random.randrange(-390, 390, 20)
        y = random.randrange(-290, 290, 20)
        food.goto(x, y)
        # add new item to the snakes body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)


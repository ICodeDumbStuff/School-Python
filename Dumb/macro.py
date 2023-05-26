import sys
import os
import turtle
import random

turtle.title("Hello")
turtle.pendown()
turtle.pencolor("blue")
turtle.screensize(512,512,"gray")


while True:
    turtle.forward(random.randint(-20, 20))
    turtle.left(random.randint(0, 360))
    turtle.speed(1000)
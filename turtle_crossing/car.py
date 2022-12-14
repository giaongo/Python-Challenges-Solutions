from turtle import Turtle
import random


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.random_color()
        self.random_position()

    def random_color(self):
        rand_r = random.randint(0, 255)
        rand_g = random.randint(0, 255)
        rand_b = random.randint(0, 255)
        self.color(rand_r, rand_g, rand_b)

    def random_position(self):
        rand_y = random.randint(-250, 250)
        self.goto(x=300, y=rand_y)

    def move_forward(self):
        self.setheading(180)
        self.forward(15)

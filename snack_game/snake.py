import random
from turtle import Turtle, Screen

DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        screen = Screen()
        screen.colormode(255)
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        snake = Turtle(shape="square")
        snake.penup()
        snake.color((r, g, b))
        snake.goto(position)
        self.snake_body.append(snake)

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def collide_with_tail(self):
        for element in self.snake_body[1:]:
            if self.head.distance(element) < 10:
                return True
        return False

    def reset(self):
        for seg in self.snake_body:
            seg.hideturtle()
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

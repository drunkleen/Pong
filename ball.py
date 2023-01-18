from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.move_x = 0.4 * random.choice([-1, 1])
        self.move_y = 0.3 * random.choice([-1, 1])

    def move(self):
        if (self.screen_height / 2 - 20) * 1 < self.ycor() + 10 or \
                (self.screen_height / 2 - 20) * -1 > self.ycor() - 10:
            self.move_y *= -1

        x = self.xcor() + self.move_x
        y = self.ycor() + self.move_y
        self.goto(x, y)

    def hit_paddle(self):
        self.move_x += random.uniform(0.055, 0.1)
        self.move_y += random.uniform(0.055, 0.1)
        print(self.move_x, self.move_y)
        self.move_x *= -1

    def reset(self):
        self.goto(0, 0)
        self.move_x = 0.3 * random.choice([-1, 1])
        self.move_y = 0.2 * random.choice([-1, 1])

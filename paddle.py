from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width

        self.shape("square")
        self.color((255, 255, 255))
        self.penup()
        if screen_width > 0:
            self.goto((screen_width / 2 - 50) * -1, 0)
        else:
            self.goto((screen_width / 2 + 50) * -1, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if (self.screen_height / 2 - 20) * 1 > self.ycor() + 60:
            y = self.ycor() + 20
            self.sety(y)

    def go_down(self):
        if (self.screen_height / 2 - 20) * - 1 < self.ycor() - 60:
            y = self.ycor() - 20
            self.sety(y)

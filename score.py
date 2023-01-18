from turtle import Turtle


class SetupScreen(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.hideturtle()
        self.color((255, 255, 255))
        self.penup()
        self.setheading(270)
        self.goto(0, screen_height / 2 - 120)
        while True:
            if ((screen_height / 2 - 20) * -1) + 15 > self.ycor():
                break
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)
        self.goto((screen_width / 2 - 20) * 1, (screen_height / 2 - 20) * 1)
        self.pendown()
        self.goto((screen_width / 2 - 20) * -1, (screen_height / 2 - 20) * 1)
        self.goto((screen_width / 2 - 20) * -1, (screen_height / 2 - 20) * -1)
        self.goto((screen_width / 2 - 20) * 1, (screen_height / 2 - 20) * -1)
        self.goto((screen_width / 2 - 20) * 1, (screen_height / 2 - 20) * 1)
        self.penup()
        self.goto(0, screen_height / 2 - 80)
        self.pendown()
        self.write('Score', align="center", font=("Courier", 24, "normal"))


class ScoreBoard(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.hideturtle()
        self.p_left_score = 0
        self.p_right_score = 0
        self.color((255, 255, 255))
        self.penup()
        self.goto(0, screen_height / 2 - 120)
        self.pendown()
        self.write(f'{self.p_left_score} - {self.p_right_score}', align="center", font=("Courier", 24, "normal"))

    def l_score_up(self):
        self.p_right_score += 1
        self.clear()
        self.write(f'{self.p_left_score} - {self.p_right_score}', align="center", font=("Courier", 24, "normal"))

    def r_score_up(self):
        self.p_left_score += 1
        self.clear()
        self.write(f'{self.p_left_score} - {self.p_right_score}', align="center", font=("Courier", 24, "normal"))



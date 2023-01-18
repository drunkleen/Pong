from turtle import Turtle, Screen
from paddle import Paddle
from score import SetupScreen, ScoreBoard
from ball import Ball
import time

screen_width = 1300
screen_height = 800

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.colormode(255)
screen.bgcolor((0, 0, 0))
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle(screen_width * -1, screen_height)
paddle_left = Paddle(screen_width, screen_height)
setup_screen = SetupScreen(screen_width, screen_height)
score = ScoreBoard(screen_width, screen_height)

ball = Ball(screen_width, screen_height)

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")
screen.update()

game_running = True
while game_running:
    time.sleep(0.001)
    screen.update()
    ball.move()

    # if player hit the ball
    if ball.distance(paddle_right) < 50 and ball.xcor() > screen_width / 2 - 60:
        ball.hit_paddle()
    elif ball.distance(paddle_left) < 50 and ball.xcor() < (screen_width / 2 - 60) * -1:
        ball.hit_paddle()
    # if score
    elif ball.xcor() > (screen_width / 2 - 20):
        score.l_score_up()
        ball.reset()
    elif ball.xcor() < (screen_width / 2 - 20) * -1:
        score.r_score_up()
        ball.reset()

screen.mainloop()

from turtle import Turtle  , Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
scoreboard = Scoreboard()

r_paddle = Paddle((350 , 0))
l_paddle = Paddle((-350 , 0))
ball = Ball()







screen.listen()
screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down ,"Down")

screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down ,"s")





screen.bgcolor("black")
screen.setup(width=800 , height= 600)
screen.title("Pong Game")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detection the collision with the wall
    if ball.ycor() > 280 or ball.ycor () < -280:
        ball.bounce_y()
        
    # collision with  paddle
    if ball.distance(r_paddle)< 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detection when the ball missies the paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    

screen.exitonclick()

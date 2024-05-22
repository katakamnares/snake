from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake Game")
game_on=True
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segements[0].distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.update()
    if snake.segements[0].xcor()>280 or snake.segements[0].xcor()<-280 or snake.segements[0].ycor()>280 or snake.segements[0].ycor()<-280:
        scoreboard.game_over()
        game_on=False
    for segement in snake.segements[1:]:
        if snake.segements[0].distance(segement)<10:
            scoreboard.game_over()
            game_on=False
    screen.listen()
    screen.onkey(key="Up",fun=snake.up)
    screen.onkey(key="Down",fun=snake.Down)
    screen.onkey(key="Right",fun=snake.Right)
    screen.onkey(key="Left",fun=snake.Left)

screen.exitonclick()


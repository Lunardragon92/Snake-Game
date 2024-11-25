from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food =Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")



is_game_on = True
while is_game_on:

    time.sleep(0.1)
    snake.move()
    screen.update()
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        score.track()
        snake.extend()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        score.reset()
    for segments in snake.segment[1:]:
        if snake.head.distance(segments)<10:
            snake.reset()
            score.reset()





screen.exitonclick()
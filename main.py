import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)

car_manager = CarManager()
player = Player()

scoreboard = Scoreboard()
scoreboard.write_score()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.new_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 23:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.goto(0, -280)
        car_manager.level_up()
        scoreboard.update()
        scoreboard.write_score()

screen.exitonclick()
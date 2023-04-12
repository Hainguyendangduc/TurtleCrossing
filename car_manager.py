COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
from random import randint, choice


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        random = randint(1, 6)
        if random == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(300, randint(-250, 250))
            car.color(choice(COLORS))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

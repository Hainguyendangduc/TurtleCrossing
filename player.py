STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() != -280:
            self.backward(MOVE_DISTANCE)

    # def level(self):
    #     if self.ycor() > FINISH_LINE_Y:
    #         self.goto(0, -280)


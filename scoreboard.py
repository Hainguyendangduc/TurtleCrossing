FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.color("red")
        self.penup()
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(arg=f"Score: {self.score}", font=FONT)
        self.goto(-280, 230)
        self.write(arg=f"Level: {self.level}", font=FONT)

    def update(self):
        self.score += (self.level * 10)
        self.level += 1

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align='center', font=("Arial", 15, "bold"))
        self.goto(0, -30)
        self.write(arg=f"Score: {self.score}", align='center', font=FONT)

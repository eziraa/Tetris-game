
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-100, 270)
        self.speed("fastest")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.score_update_level = 0
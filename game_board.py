# Importing important  packages
from turtle import Turtle, Screen
import random
import time

# Declaring global object
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
tetris_compnnts_list = []


# Class game board
class GameBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(500, 600)
        self.screen.bgcolor("black")
        self.screen.listen()

    def start(self):
        pass

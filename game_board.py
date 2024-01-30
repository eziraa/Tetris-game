# Importing important  packages
from turtle import Turtle, Screen

from o_block import OBlock
from t_block import TBlock
from l_block import LBlock
from j_block import JBlock
from z_block import ZBlock
from s_block import SBlock
import random
import time

# Declaring global object
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

# List that contain class of tetris blocks
tetris_blocks_list = [SBlock]


# Class game board
class GameBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(500, 600)
        self.screen.bgcolor("black")

        # make screen event consumer
        self.screen.listen()
        self.is_game_on = True

        # get the current tetris block
        self.current = random.choice(tetris_blocks_list)()

    def start(self):
        while self.is_game_on:
            self.screen.update()
        self.screen.exitonclick()

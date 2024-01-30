import time

from turtle import Turtle


class TetrisBlock(Turtle):
    def __init__(self):
        super().__init__()
        self.tetris_block_segments = []
        self.hideturtle()

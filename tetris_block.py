import time
from abc import ABC, abstractmethod
from turtle import Turtle


class TetrisBlock(Turtle, ABC):
    def __init__(self):
        super().__init__()
        self.tetris_block_segments = []
        self.hideturtle()
        self.front = []
        self.head = []
        self.right = []
        self.left = []

import time

from abc import ABC, abstractmethod
from turtle import Turtle


class TetrisBlock(Turtle):
    def __init__(self):
        super().__init__()
        self.tetris_block_segments = []
        self.hideturtle()
        self.front = []
        self.head = []
        self.right = []
        self.left = []

    def startMove(self):
        for segment in self.tetris_block_segments:
            segment.forward(22)

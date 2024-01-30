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

    # Abstract methods

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def set_up(self):
        pass

    @abstractmethod
    def update_set_left(self):
        pass

    @abstractmethod
    def update_set_right(self):
        pass

    @abstractmethod
    def update_set_down(self):
        pass

    @abstractmethod
    def update_set_up(self):
        pass

    def startMove(self):
        for segment in self.tetris_block_segments:
            segment.forward(22)

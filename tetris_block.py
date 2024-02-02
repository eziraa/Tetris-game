import time

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
        self.center = 0
        self.rotate_index = 0
        self.rotate_position = []

    def startMove(self):
        for segment in self.tetris_block_segments:
            segment.forward(22)

    def rotate(self):
        position = self.rotate_position[self.rotate_index]()
        for i in range(len(position)):
            self.tetris_block_segments[i].goto(position[i])
        front = self.front
        self.front.clear()
        self.front.extend(self.right)
        self.right.clear()
        self.right.extend(self.head)
        self.head.clear()
        self.head.extend(self.left)
        self.left.clear()
        self.left.extend(front)

        
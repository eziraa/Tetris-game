from abc import ABC

from tetris_block import TetrisBlock
from turtle import Turtle

# indicating the position of tetris block segments
POSITION_LIST = [(-20, 270), (2, 270), (2, 292), (2, 314)]


class JBlock(TetrisBlock):
    def __init__(self):
        super().__init__()
        self.create()
        self.set_up()

    def create(self):
        """
        This method is to create segments of JBlock"""
        for position in POSITION_LIST:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("purple")
            new_segment.speed("fastest")
            new_segment.goto(position)
            self.tetris_block_segments.append(new_segment)

    def set_up(self):
        """
        This method used to separate head,  fron, left and right of JBlock"""
        self.front.extend([self.tetris_block_segments[0], self.tetris_block_segments[1]])
        self.head.extend([self.tetris_block_segments[0], self.tetris_block_segments[3]])
        self.left.extend([self.tetris_block_segments[0], self.tetris_block_segments[2], self.tetris_block_segments[3]])
        self.right.extend([self.tetris_block_segments[3], self.tetris_block_segments[2], self.tetris_block_segments[1]])
        self.center = self.tetris_block_segments[2]
        for segment in self.tetris_block_segments:
            segment.setheading(270)
            
    def getPosition(self):
        x = round(self.center.xcor())
        y = round(self.center.ycor())
        position = []
        if self.rotate_index == 0:
            position = [(x - 22, y + 22), (x - 22, y), (x, y), (x + 22, y)]
            self.rotate_index = 1
        elif self.rotate_index == 1:
            position = [(x + 22, y + 22), (x, y + 22), (x, y), (x, y - 22)]
            self.rotate_index = 2
        elif self.rotate_index == 2:
            position = [(x + 22, y - 22), (x + 22, y), (x, y), (x - 22, y )]
            self.rotate_index = 3
        else:
            position = [(x - 22, y - 22), (x, y - 22), (x, y), (x, y + 22)]
            self.rotate_index = 0
        return position
        
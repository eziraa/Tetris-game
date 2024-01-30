from turtle import Turtle
from tetris_block import TetrisBlock

POSITION_LIST = [(24, 270), (24, 292), (2, 292), (2, 314)]


class ZBlock(TetrisBlock):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        for position in POSITION_LIST:
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('green')
            new_segment.speed("fastest")
            new_segment.goto(position)
            self.tetris_block_segments.append(new_segment)
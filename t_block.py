from tetris_block import TetrisBlock
from turtle import Turtle

POSITION_LIST = [(-20, 270), (2, 270), (24, 270), (2, 292)]


class TBlock(TetrisBlock):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        for position in POSITION_LIST:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("orange")
            new_segment.speed("fastest")
            new_segment.goto(position)
            self.tetris_block_segments.append(new_segment)

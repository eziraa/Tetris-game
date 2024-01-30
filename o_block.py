from turtle import Turtle
from tetris_block import TetrisBlock

# to indicate the position of individual segment of the block

POSITION_LIST = [(-20, 270), (2, 270), (2, 292), (-20, 292)]


class OBlock(TetrisBlock):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        for position in POSITION_LIST:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.speed("fastest")
            new_segment.goto(position)
            self.tetris_block_segments.append(new_segment)


from tetris_block import TetrisBlock
from turtle import Turtle

# indicating the position of tetris block segments
POSITION_LIST = [(-20, 270), (2, 270), (2, 292), (2, 314)]


class JBlock(TetrisBlock):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        for position in POSITION_LIST:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("purple")
            new_segment.speed("fastest")
            new_segment.goto(position)
            self.tetris_block_segments.append(new_segment)

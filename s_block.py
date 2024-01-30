from turtle import Turtle
from tetris_block import TetrisBlock

# to indicating the correct position of this block segment
POSITION_LIST = [(-20, 270), (-20, 292), (2, 292), (2, 314)]


class SBlock(TetrisBlock):
    
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        for position in POSITION_LIST:
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('blue')
            new_segment.speed("fastest")
            new_segment.goto(position)
            self.tetris_block_segments.append(new_segment)
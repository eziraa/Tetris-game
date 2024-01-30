from turtle import Turtle
from tetris_block import TetrisBlock

# To indicating the correct position of the individual segments of this block
POSITION_LIST = [(2, 270), (2, 292), (2, 314), (2, 336)]


# Creating class OneBlock
class OneBlock(TetrisBlock):
    def __init__(self):
        super().__init__()
        self.create()

    # Implementing create method to create ui of the block
    def create(self):
        for position in POSITION_LIST:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color('red')
            new_segment.speed("fastest")
            new_segment.goto(position)
            self.tetris_block_segments.append(new_segment)

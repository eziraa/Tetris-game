from turtle import Turtle
from tetris_block import TetrisBlock

# To indicating the correct position of the individual segments of this block
POSITION_LIST = [(2, 270), (2, 292), (2, 314), (2, 336)]


# Creating class OneBlock
class IBlock(TetrisBlock):
    def __init__(self):
        super().__init__()
        self.create()
        self.set_up()
        # self.rotate_position = [self.rotateFirst]

    # Implementing create method to create ui of the block
    def create(self):
        """
        This method is to create segments of I"""
        for position in POSITION_LIST:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color('red')
            new_segment.speed("fastest")
            new_segment.goto(position)
            self.tetris_block_segments.append(new_segment)

    def set_up(self):
        """
        This method used to set front, left, right, head of the Block"""
        self.front.append(self.tetris_block_segments[0])
        self.left.extend(self.tetris_block_segments)
        self.right.extend(self.tetris_block_segments)
        self.head.append(self.tetris_block_segments[3])
        self.center = self.tetris_block_segments[1]
        for segment in self.tetris_block_segments:
            segment.setheading(270)
    


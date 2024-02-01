from turtle import Turtle
from tetris_block import TetrisBlock

POSITION_LIST = [(24, 270), (24, 292), (2, 292), (2, 314)]


class ZBlock(TetrisBlock):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        """
        This method is to creae segments of ZBlock"""
        for position in POSITION_LIST:
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('green')
            new_segment.speed("fastest")
            new_segment.goto(position)
            self.tetris_block_segments.append(new_segment)
    
    def set_up(self):
        """
        This class used to separate head, front, left and right of ZBlock"""
        self.front.extend([self.tetris_list[2], self.tetris_list[0]])
        self.left.extend([self.tetris_list[0], self.tetris_list[2], self.tetris_list[3]])
        self.right.extend([self.tetris_list[0], self.tetris_list[1], self.tetris_list[3]])
        self.head.extend([self.tetris_list[3], self.tetris_list[1]])
        for segment in self.tetris_list:
            segment.setheading(270)

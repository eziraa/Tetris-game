from tetris_block import TetrisBlock
from turtle import Turtle

POSITION_LIST = [(-20, 270), (2, 270), (24, 270), (2, 292)]


class TBlock(TetrisBlock):
    def __init__(self):
        super().__init__()
        self.create()
        self.set_up()

    def create(self):
        """
        This method is to create segment of TBlock """
        for position in POSITION_LIST:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("orange")
            new_segment.speed("fastest")
            new_segment.goto(position)
            self.tetris_block_segments.append(new_segment)
            
    def set_up(self):
        """
        This method is to seprate head, front, left and right of TBlock """
        self.front.extend([self.tetris_list[0], self.tetris_list[1], self.tetris_list[2]])
        self.left.extend([self.tetris_list[0], self.tetris_list[3]])
        self.head.extend([self.tetris_list[0], self.tetris_list[2], self.tetris_list[3]])
        self.right.extend([self.tetris_list[3], self.tetris_list[2]])
        for segment in self.tetris_list:
            segment.setheading(270)

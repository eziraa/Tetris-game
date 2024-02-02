from tetris_block import TetrisBlock
from turtle import Turtle

# indicating the position of tetris block segments
POSITION_LIST = [(24, 270), (2, 270), (2, 292), (2, 314)]


class LBlock(TetrisBlock):
    def __init__(self):
        super().__init__()
        self.create()
        self.set_up()
        self.rotate_position = [self.rotateFirst, self.rotateSecond]

    
    def create(self):
        """
        This method is to create segment of LBlock"""
        for position in POSITION_LIST:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("yellow")
            new_segment.speed("fastest")
            new_segment.goto(position)
            self.tetris_block_segments.append(new_segment)

    def set_up(self):
        """
        This method is to assign left, head, front, right segment of LBlock"""
        self.front.extend([self.tetris_block_segments[0], self.tetris_block_segments[1]])
        self.head.extend([self.tetris_block_segments[0], self.tetris_block_segments[3]])
        self.left.extend([self.tetris_block_segments[3], self.tetris_block_segments[2], self.tetris_block_segments[1]])
        self.right.extend([self.tetris_block_segments[3], self.tetris_block_segments[2], self.tetris_block_segments[0]])
        self.center = self.tetris_block_segments[2]
        for segment in self.tetris_block_segments:
            segment.setheading(270)
    
    def rotateFirst(self):
        """
        This method is to get the correct position of the block when we rotate the block for first time"""
        x = round(self.center.xcor())
        y = round(self.center.ycor())
        position = [(x - 22, y - 22), (x - 22, y), (x, y), (x + 22, y)]
        self.rotate_index = 1
        return position
    
    



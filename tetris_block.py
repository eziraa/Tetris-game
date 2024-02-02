import time

from turtle import Turtle


class TetrisBlock(Turtle):
    def __init__(self):
        super().__init__()
        self.tetris_block_segments = []
        self.hideturtle()
        self.front = []
        self.head = []
        self.right = []
        self.left = []
        self.center = 0
        self.rotate_index = 0
        self.rotate_positions = []

    def startMove(self):
        for segment in self.tetris_block_segments:
            segment.forward(22)
    
    

    def rotate(self):
        if len(self.rotate_positions)  == 0:
            return 
        position = self.getPosition()
        for i in range(len(position)):
            self.tetris_block_segments[i].goto(position[i])
        front = self.front
        self.front.clear()
        self.front.extend(self.right)
        self.right.clear()
        self.right.extend(self.head)
        self.head.clear()
        self.head.extend(self.left)
        self.left.clear()
        self.left.extend(front)
    
    def getPosition(self):
        """
        This method is to get the next position when we rotate the block"""
        x = round(self.center.xcor())
        y = round(self.center.ycor())
        position = []
        for pos in self.rotate_positions[self.rotate_index]:
            position.append((x + pos[0], y + pos[1]))
        self.rotate_index = self.rotate_index + 1 if self.rotate_index < len(self.rotate_positions) - 1 else 0
        return position

        
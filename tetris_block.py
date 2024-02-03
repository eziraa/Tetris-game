import time

from turtle import Turtle
from terminated_block_segments import terminated_segments

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
        self.terminated = False

    def startMove(self):
        for segment in self.tetris_block_segments:
            segment.forward(22)
    
    

    def rotate(self):
        if len(self.rotate_positions)  == 0:
            return 
        position = self.getPosition()
        if not TetrisBlock.no_neighbour(position):
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

    @staticmethod
    def no_neighbour(position):
        x_coordinate = set()
        y_coordinate = set()
        for elem in terminated_segments:
            x_coordinate.add(round(elem.xcor()))
            y_coordinate.add(round(elem.ycor()))
        x_coordinate = list(x_coordinate)
        y_coordinate = list(y_coordinate)
        illegal = False
        for item in position:
            for coordinate in y_coordinate:
                for coordinate_x in x_coordinate:
                    if round(item[0]) == coordinate_x and round(item[1]) == coordinate:
                        illegal = True
                        break
        return illegal
    
    def move_left(self):
        is_near = False
        for item in self.tetris_block_segments:
            for head in terminated_segments:
                if round(abs(item.xcor() - head.xcor())) == 22 and abs(item.ycor() - head.ycor()) < 1:
                    is_near = True
                    break
            if item.xcor() <= -230:
                is_near = True
                break
        if not is_near:
            for item in self.tetris_block_segments:
                item.goto((item.xcor() - 22, item.ycor()))

    def move_right(self):
        is_near = False
        for item in self.tetris_block_segments:
            for head in terminated_segments:
                if round(abs(item.xcor() - head.xcor())) == 22 and abs(item.ycor() - head.ycor()) < 1:
                    # if head.distance(item) <= 23:
                    is_near = True
                    break
            if item.xcor() > 220:
                is_near = True
                break

        if not is_near:
            for item in self.tetris_block_segments:
                item.goto((item.xcor() + 22, item.ycor()))
    
    def move_last(self):
        while not self.terminated:
            for item in self.front:
                if not self.terminated:
                    for head in terminated_segments:
                        if round(abs(item.ycor() - head.ycor())) == 22 and abs(item.xcor() - head.xcor()) < 1:
                            self.terminated = True
                            break
                    if item.ycor() < -270:
                        self.terminated = True
                        break
            if not self.terminated:
                self.startMove()
        

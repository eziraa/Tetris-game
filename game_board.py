# Importing important  packages
from turtle import Turtle, Screen

from o_block import OBlock
from t_block import TBlock
from l_block import LBlock
from j_block import JBlock
from z_block import ZBlock
from s_block import SBlock
from i_block import IBlock
from terminated_block_segments import terminated_segments
import random
import time

# Declaring global object
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

# List that contain class of tetris blocks
TETRIS_BLOCKS_LIST = [LBlock, SBlock, ZBlock, TBlock, IBlock,JBlock, OBlock]


# Class game board
class GameBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(500, 600)
        self.screen.bgcolor("black")

        # make screen event consumer
        self.screen.listen()
        self.is_game_on = True
        self.terminated_segments = terminated_segments
        # get the current tetris block
        self.current = random.choice(TETRIS_BLOCKS_LIST)()

    def start(self):
        while self.is_game_on:
            time.sleep(0.2)
            self.screen.update()
            self.current.startMove()
            self.screen.onkey(self.current.rotate , 'Up')
            self.screen.onkey(self.current.move_left , 'Left')
            self.screen.onkey(self.current.move_right , 'Right')
            
            for item in self.current.front:
                if not self.current.terminated:
                    for head in self.terminated_segments:
                        if round(abs(item.ycor() - head.ycor())) == 22 and abs(item.xcor() - head.xcor()) < 1:
                            self.current.terminated = True
                            break
                    if item.ycor() < -270:
                        self.current.terminated = True
                        break
                else:
                    for segment in self.current.tetris_block_segments:
                        if segment.ycor() > 270:
                            tim = Turtle()
                            tim.color('white')
                            tim.write("GAME OVER!!!", align="center", font=("Arial", 24, "normal"))
                            tim.hideturtle()
                            self.is_game_on = False
            
            if self.current.terminated:
                self.terminated_segments.extend(self.current.tetris_block_segments)
                self.current.terminated = False       
                self.current = LBlock() 
        self.screen.exitonclick()

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
from score_board import ScoreBoard
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
        self.is_game_on = True
        self.terminated_segments = terminated_segments
        # get the current tetris block
        self.current = random.choice(TETRIS_BLOCKS_LIST)()
        self.score_board = ScoreBoard()
        self.fast_level = 0.3
        self.set_up()

    def start(self):
        self.screen.listen()
        while self.is_game_on:
            time.sleep(self.fast_level)
            self.addEventListeners()
            self.screen.update()
            if not self.current.terminated:
                self.current.startMove()
            self.checkTerminated()
            self.checkGameOver()
            if self.current.terminated:
                self.getNewBlock()
            self.updateScoreBoard()
        self.screen.exitonclick()
    
    def addEventListeners(self):
        self.screen.onkey(self.current.rotate , 'Up')
        self.screen.onkey(self.current.move_left , 'Left')
        self.screen.onkey(self.current.move_right , 'Right')
        self.screen.onkey(self.current.move_last , 'Down')
    
    def checkTerminated(self):
        for item in self.current.front:
            if not self.current.terminated:
                for head in self.terminated_segments:
                    if round(abs(item.ycor() - head.ycor())) == 22 and abs(item.xcor() - head.xcor()) < 1:
                        self.current.terminated = True
                        break
                if item.ycor() < -270:
                    self.current.terminated = True
                    break
    def checkGameOver(self):
        for segment in self.terminated_segments:
            if segment.ycor() > 270:
                tim = Turtle()
                tim.color('white')
                tim.write("GAME OVER!!!", align="center", font=("Arial", 24, "normal"))
                tim.hideturtle()
                self.is_game_on = False
    def getNewBlock(self):
        self.terminated_segments.extend(self.current.tetris_block_segments)
        self.current.terminated = False       
        self.current =random.choice(TETRIS_BLOCKS_LIST)()         
    
    def updateScoreBoard(self):
        y_coordinate = set()
        for segment in self.terminated_segments:
            y_coordinate.add(round(segment.ycor()))
        y_coordinate = list(y_coordinate)
        for y in range(len(y_coordinate)):
            x_coordinate = set()
            for item in self.terminated_segments:
                if round(item.ycor()) == y_coordinate[y]:
                    x_coordinate.add(item)
            x_coordinate = list(x_coordinate)
            if len(x_coordinate) == 22:
                self.score_board.update_score()
                for item in x_coordinate:
                    item.hideturtle()
                    self.terminated_segments.remove(item)
                for item in self.terminated_segments:
                    if round(item.ycor()) > y_coordinate[y]:
                        item.setheading(270)
                        item.forward(22)   
                             
    def set_up(self):
        while True:
            text = self.screen.textinput("Choose the level of the game",
                                         "1. level 1 \n2. level 2 \n3. level 3 \n4. level 4 \n5. level 5 \n6. level 6 \n7. level 7")
            if text is None:
                exit()
            elif text.isdigit() and 0 < int(text) <= 7:
                self.fast_level = 0.7 if text == '1' else 0.6 if text == '2' else 0.5 if text == '3' else 0.4 if text == '4' else 0.3 if text == '5' else 0.2 if text == '6' else 0.1
                self.score_board.score_update_level = 4 if text == '1' else 5 if text == '2' else 6 if text == '3' else 7 if text == '4' else 8 if text == '5' else 9 if text == '6' else 10
                break
    
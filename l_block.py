from tetris_block import TetrisBlock
from turtle import Turtle

POSITION_LIST = [(24, 270), (2, 270), (2, 292), (2, 314)]


class LBlock(TetrisBlock):
    def __init__(self):
        super().__init__()

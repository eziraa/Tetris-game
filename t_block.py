from tetris_block import TetrisBlock
from turtle import Turtle

POSITION_LIST = [(-20, 270), (2, 270), (24, 270), (2, 292)]


class TBlock(TetrisBlock):
    def __init__(self):
        super().__init__()

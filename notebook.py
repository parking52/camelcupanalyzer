from __future__ import division
__author__ = 'melchior'
import random
import time
import numpy
from board import Board


board = Board(20)

print(board.board)
print("----------------------------------------------")

# board.board_init()
board.board_init(config=True)
print(board.board)
print("----------------------------------------------")

# board.play_camel(3)

board.loop_until_end()

print(board.board)
print("----------------------------------------------")



print(board.camel_list)
print(board.compute_prob_for_each_camel())




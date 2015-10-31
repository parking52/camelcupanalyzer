from __future__ import division
__author__ = 'melchior'
import random
import time
import numpy
from board import Board


board = Board(16)

print(board.board)

board.play_camel(3)
print(board.board)

print(board.camel_list)
print(board.compute_prob_for_each_camel())




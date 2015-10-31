from __future__ import division
__author__ = 'melchior'
import random
import time
import numpy
from board import Board
import matplotlib.pyplot as plt

board = Board(20)

# print(board.board)
# print("----------------------------------------------")

# board.board_init()
board.board_init(config=True)
print(board.board)
print("----------------------------------------------")

# board.play_camel(3)

board.loop_until_end()
winner_list = []
for i in range(100000):
    board = Board(20)
    board.board_init(config=True)
    winner_list.append(board.loop_until_end())

print(winner_list)
print("----------------------------------------------")


plt.hist(winner_list)
plt.title("Camel victory chances")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
plt.savefig('camel_hist' + str(time.clock()) + '.png')



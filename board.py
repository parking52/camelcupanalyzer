from __future__ import division
__author__ = 'melchior'
import random
import time
import numpy
from camel import Camel
from collections import deque

class Board():

    def __init__(self, n):
        self.board = numpy.zeros(shape=(n, 5))
        self.camel_list = [Camel(1), Camel(2), Camel(3), Camel(4), Camel(5)]

        # for camel in self.camel_list:
        #     self.add_camel_on_top_of_case_n(camel, 0)


    def play_camel(self, n):

        dice = random.randint(1, 3)
        list_of_case = self.board[self.camel_list[n-1].position]
        index_of_camel_on_case = numpy.where(list_of_case == self.camel_list[n-1].camel_numero)[0]
        number_of_moving_camels = list_of_case[:(index_of_camel_on_case+1)]
        stack_of_moving_camels = [self.camel_list[int(i-1)] for i in number_of_moving_camels]

        for camel in reversed(stack_of_moving_camels):
            self.add_camel_on_top_of_case_n(camel, camel.position + dice)
            self.remove_camel_n_from_position(camel, camel.position)
            camel.position = camel.position + dice


    def compute_prob_for_each_camel(self):

        result_array = [0, 1, 0, 0, 0]

        return result_array

    def remove_camel_n_from_position(self, camel, n):

        tile_state = self.board[n]
        index = numpy.where(tile_state == camel.camel_numero)[0]
        self.board[n][index] = 0
        index += 1

        while index < 5:
            self.board[n][index - 1] = self.board[n][index]
            self.board[n][index] = 0
            index += 1


    def add_camel_on_top_of_case_n(self, camel, n):
        self.board[n][4] = self.board[n][3]
        self.board[n][3] = self.board[n][2]
        self.board[n][2] = self.board[n][1]
        self.board[n][1] = self.board[n][0]
        self.board[n][0] = camel.camel_numero


    def board_init(self, config=None):

        if config == None:

            random.shuffle(self.camel_list)

            for camel in self.camel_list:
                dice = random.randint(1, 3) - 1 ## can start at 0
                self.add_camel_on_top_of_case_n(camel, dice)
                camel.position += dice

        else:
            starting_places = [[1, 3], [2, 3], [0, 2], [2, 1], [4, 2]]
            for starting_place in starting_places:
                # self.camel_list[starting_place[0]].position = starting_place[1]
                self.add_camel_on_top_of_case_n(self.camel_list[starting_place[0]], starting_place[1])



    def loop_until_end(self):

        while self.no_position_over_16():
            pass

    def no_position_over_16(self):
        for camel in self.camel_list:
            if camel.position >= 16:
                return camel.position


        return false














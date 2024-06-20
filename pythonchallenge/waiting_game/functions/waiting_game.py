# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 00:36:32 2023

@author: Ludovico
"""
from time import perf_counter
from random import randint


target_time = randint(1, 5)


def waiting_game(target_time):
    print("the target time is {:0.1f} sec, good luck!".format(target_time))
    enter = input("Press Enter to Start, 0 to exit: ")
    if enter == '':
        start_time = perf_counter()
        stop = input("press Enter to Stop: ")
        if stop == '':
            elapsed_time = perf_counter()
            velocity = elapsed_time-start_time
            print("Your velocity was:{:.1f} sec \n".format(velocity))
            if (-0.1 <= target_time-velocity <= 0.1):
                print("congratulations! right on target")
                return 0
            elif target_time-velocity > 0.1:
                print("Too fast try again")
                return waiting_game(target_time)
            elif target_time-velocity < -0.1:
                print("too slow try again")
                return waiting_game(target_time)
    else:
        if enter == 0:
            print('*****goodbay*****')
            exit
h = waiting_game(target_time)
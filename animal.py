from random import randint as rand
import math
import pygame

from gameconst import *

class Animal:
    def __init__(self, x, y):
        self.MAX_AGE = 120
        self.REPRODUCT_AGE = self.MAX_AGE - int(self.MAX_AGE*0.8)
        self.x = x
        self.y = y
        self.dir = 0    # 0 N, 1 NE, .., 5 S, .., 8 NW
        self.age = 0
        self.brain0 = [rand(0, 100)/100. for _ in range(9)]
        # self.brain1 = [rand(0, 100)/100. for _ in range(10)]

    def get_environ(self, in_list):
        for i in in_list:
            pass

    def go_forward(self):
        pass
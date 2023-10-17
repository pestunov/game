from random import randint as rand
import math
import pygame

from gameconst import *
from trees import Tree
from animal import Animal


class World:
    def __init__(self, w, h, screen):
        self.width = w
        self.height = h
        self.screen = screen
        self.area = self.width * self.height
        self.trees_list = [0 for _ in range(self.area)]
        self.fert_list = [0 for _ in range(self.area)]

    def seed(self, quantity):
        for i in range(quantity):
            x = rand(0, self.width)
            y = rand(0, self.height)
            self._plant_seed(x, y)

    def step(self):
        for i, item in enumerate(self.trees_list):
            if type(item) == Tree:
                if item.telomera <= 0:
                    self.trees_list[i] = 0
                    continue
                item.grow()
                for _ in range(item.have_seeds):
                    x = item.x + rand(-2, 2)
                    y = item.y + rand(-2, 2)
                    self._plant_seed(x, y)

                item.show(self.screen)

    def _plant_seed(self, x, y):
        while x < 0:
            x = CELLS_WIDTH + x
        while x >= CELLS_WIDTH:
            x = x - CELLS_WIDTH
        while y < 0:
            y = CELLS_HEIGHT + y
        while y >= CELLS_HEIGHT:
            y = y - CELLS_HEIGHT
        if type(self.trees_list[y * CELLS_WIDTH + x]) != Tree:
            self.trees_list[y * CELLS_WIDTH + x] = Tree(x ,y)
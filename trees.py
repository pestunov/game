from random import randint as rand
import math
import pygame

from gameconst import *


class Tree:

    def __init__(self, x, y):
        self.MAX_AGE = rand(95, 100)
        self.x = x;
        self.y = y;
        self.age = 0
        self.telomera = self.MAX_AGE
        self.biomass = 0
        self.have_seeds = 0

    def __str__(self):
        return f"tree at {self.x}, {self.y}, aged {self.age}!"

    def grow(self):
        self.age += 1
        self.telomera -= 1
        self.biomass += 1
        if self.age in [x for x in range(10, 60, 5)]:
            self.have_seeds += rand(0, 2)

    def show(self, screen):
        xx = self.x * CELL_SIZE
        yy = self.y * CELL_SIZE
        if self.telomera < 1:
            color = 0x301000
        else:
            color = (abs(int(self.age)) << 16) |\
                    (abs(int(self.telomera/self.MAX_AGE*256)) << 8) |\
                    (0 << 0)
        pygame.draw.circle(screen, color, (xx, yy), math.isqrt(self.biomass)/1.5, 0)


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
                if item.telomera < 0:
                    self.trees_list[i] = 0
                    continue
                item.grow()
                for i in range(item.have_seeds):
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
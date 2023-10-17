from random import randint as rand
import math
import pygame

from gameconst import *


class Tree:

    def __init__(self, x, y):
        self.MAX_AGE = rand(80, 100)
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
        if self.age in [x for x in range(10, 80, 5)]:
            self.have_seeds += rand(0, 3)

    def show(self, screen):
        xx = self.x * CELL_SIZE
        yy = self.y * CELL_SIZE
        size = int(math.sqrt(self.biomass))
        color = (abs(int(self.age)) << 16) | \
                (abs(int(self.telomera/self.MAX_AGE*256)) << 8) | \
                (0)

        # pygame.draw.circle(screen, color, (xx, yy), math.isqrt(self.biomass)/1.5, 0)
        pygame.draw.rect(screen, color, (xx-size/2, yy-size/2, size, size), 0)

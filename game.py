#!/usr/bin/python3
"""
Created on Mon Nov 16 08:16:12 2020

@author: Phil
"""

import pygame as pg
import os

from gameconst import *

from world import World

CUR_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(CUR_FOLDER, 'images')

pg.init()
pg.display.set_caption('Hello pygame')
mainScreen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

world = World(CELLS_WIDTH, CELLS_HEIGHT, mainScreen)
world.seed(3)

# Цикл игры
game = True
while game:
    for e in pg.event.get():
        # check for closing window
        if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
            game = False
    world.step()
    # Keep tempo
    clock.tick(FPS)
    pg.display.flip()

pg.quit()


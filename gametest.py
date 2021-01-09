#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 08:16:12 2020

@author: Phil
"""

import pygame as pg
import os

from characters import Cell, Player
from gamelevels import *
from gameconst import *


CUR_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(CUR_FOLDER, 'images')


def worldCreate(arr):
    wallGroup = pg.sprite.Group()
    prixGroup = pg.sprite.Group()
    enemyGroup = pg.sprite.Group()
    for _i in range(len(arr)):
        for _j in range(len(arr[_i])):
            cmi = arr[_i][_j]
            cm = imgMap[cmi]
            brick = Cell(_j*16, _i*16, imgKit[cm], cmi)
            if cmi == 'b' or cmi == 'c':
                wallGroup.add(brick)
            elif cmi == 't' or cmi == 'd':
                prixGroup.add(brick)
    return wallGroup, prixGroup, enemyGroup
            
def worldPhisics(hero):
    res = pg.sprite.spritecollide(hero, wallGroup, dokill = False)
    if len(res) != 0:
        if hero.goRight:
            hero.goRight = False
    res = pg.sprite.spritecollide(hero, prixGroup, dokill = True)
    
    for i in res:
        print(i.tag, end='')
    pass
#     whoCollide = hero0.rect.collidelist(brickRectsList)
#     if whoCollide != -1:
#         if bricksList[whoCollide].tag == 'b':
#             print('.', end='')
#             hero0.xx -= hero0.speedX
#             hero0.yy -= hero0.speedY
#         if bricksList[whoCollide].tag == 't':
#             bricksList[whoCollide].destroy()
#             brickRectsList[whoCollide] = None
#             print('tyns')
            


################################

### Let's Game to be started ###

################################
            
pg.init()
pg.display.set_caption('Hello pygame')
mainScreen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
imge = pg.image.load(os.path.join(IMG_FOLDER, 'colored_packed.png')).convert_alpha()
imgKit = []
for i in range(22):
    for j in range(48):
        imgKit.append(imge.subsurface(j*16, i*16, 16, 16))


player1 = Player(16, 16, imgKit[25])

brickRectsList = []
bricksList = []
wallGroup, prixGroup, enemyGroup = worldCreate(levels[0])

# Цикл игры
game = True
while game:
    # Keep tempo
    clock.tick(FPS)
    # check for events
    for e in pg.event.get():
        # check for closing window
        if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
            game = False
        if e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
            player1.goLeft = True
        elif e.type == pg.KEYUP and e.key == pg.K_LEFT:
            player1.goLeft = False
        elif e.type == pg.KEYDOWN and e.key == pg.K_RIGHT:
            player1.goRight = True
        elif e.type == pg.KEYUP and e.key == pg.K_RIGHT:
            player1.goRight = False
        elif e.type == pg.KEYDOWN and e.key == pg.K_UP:
            player1.goUp = True
        elif e.type == pg.KEYUP and e.key == pg.K_UP:
            player1.goUp = False
        elif e.type == pg.KEYDOWN and e.key == pg.K_DOWN:
            player1.goDown = True
        elif e.type == pg.KEYUP and e.key == pg.K_DOWN:
            player1.goDown = False

    player1.update()
    worldPhisics(player1)
    wallGroup.draw(mainScreen)
    prixGroup.draw(mainScreen)
    enemyGroup.draw(mainScreen)
    player1.draw(mainScreen)
    pg.display.flip()


pg.quit()


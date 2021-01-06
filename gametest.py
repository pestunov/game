#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 08:16:12 2020

@author: Phil
"""

import pygame as pg
import os

from gamelevels import levels, cellMap

WIDTH = 512
HEIGHT = 336
FPS = 50
PIX_FOR_BRIX = 16
STEPS_FOR_CYCLE = 16
N_STEP_FOR_TEST = 5
BLACK = (0, 0, 0)
BKGR = (0, 0, 0)

step_n = 0

goLeft = goRight = goUp = goDown = False

cur_folder = os.path.dirname(__file__)
img_folder = os.path.join(cur_folder, 'images')


class Cell(pg.sprite.Sprite):
    def __init__(self, xx, yy, img):
        pg.sprite.Sprite.__init__(self)
        self.xx = xx
        self.yy = yy
        self.image = img
        self.image.set_colorkey(BKGR)
        self.rect = self.image.get_rect(topleft=(self.xx, self.yy))


class Player(Cell):
    def __init__(self, xx, yy, img):
        super().__init__(xx, yy, img)
        self.speedX = 0
        self.speedY = 0
        self.goLeft = False
        self.goRight = False
        self.goUp = False
        self.goDown = False
        
    def update(self):
        if self.goRight:
            self.speedX = 1
            self.speedY = 0
        elif self.goLeft:
            self.speedX = -1
            self.speedY = 0
        elif self.goUp:
            self.speedX = 0
            self.speedY = -1
        elif self.goDown:
            self.speedX = 0
            self.speedY = 1
        else:
            if self.xx % PIX_FOR_BRIX == 0:
                self.speedX = 0
            if self.yy % PIX_FOR_BRIX == 0:
                self.speedY = 0
        self.xx += self.speedX
        self.yy += self.speedY
        self.rect.x = self.xx
        self.rect.y = self.yy
        bumpsI = self.rect.collidelist(brickRectsGroup)
        if bumpsI != -1:
            self.xx -= self.speedX
            self.yy -= self.speedY
            bricksGroup.remove(bumpsI)

def worldCreate(arr):
    for _i in range(len(arr)):
        for _j in range(len(arr[_i])):
            cmi = arr[_i][_j]
            cm = cellMap[cmi]
            brick = Cell(_j*16, _i*16, imgKit[cm])
            bricksGroup.add(brick)
            if (cmi==' ') or (cmi=='t'):
                pass
            else:
                brickRectsGroup.append(brick.rect)
    bricksGroup.draw(mainScreen)


### Let's Game to be started ###
pg.init()
mainScreen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Hello pygame')

clock = pg.time.Clock()

imge = pg.image.load(os.path.join(img_folder, 'colored_packed.png')).convert_alpha()
BKGR = imge.get_at((0, 0))
imgKit = []
for i in range(22):
    for j in range(48):
        imgKit.append(imge.subsurface(j*16, i*16, 16, 16))

herosGroup = pg.sprite.Group()
player1 = Player(16, 16, imgKit[25])

herosGroup.add(player1)


bricksGroup = pg.sprite.Group()
brickRectsGroup = []
worldCreate(levels[0])

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

    bricksGroup.draw(mainScreen)
    herosGroup.update()
    herosGroup.draw(mainScreen)
    pg.display.flip()


pg.quit()


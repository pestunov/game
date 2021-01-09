#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame as pg
from gameconst import *

class Collide:
    def __init__(self):
        pass


class Cell(pg.sprite.Sprite):
    def __init__(self, xx, yy, img, tag = None):
        pg.sprite.Sprite.__init__(self)
        self.xx = xx
        self.yy = yy
        self.tag = tag
        self.image = img
        _bkgrd = self.image.get_at((0, 0))
        self.image.set_colorkey(_bkgrd)
        self.rect = pg.Rect((self.xx, self.yy), (PIX_FOR_BRIX, PIX_FOR_BRIX))
        
    def destroy(self):
        self.kill()
        
    def draw(self, scr):
        scr.blit(self.image, self.rect)


class Player(Cell):
    def __init__(self, xx, yy, img):
        super().__init__(xx, yy, img)
        self.score = 0
        self.lives = 1
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

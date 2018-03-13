#!/usr/bin/env python

import pygame, sys, glob
from pygame import *

h = 800
w = 1000

screen = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()


class character:
    def __init__(self, x, y, picture_files):
        self.x = x
        self.y = y
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init

        self.ani = glob.glob(picture_files)
        self.ani.sort()

        self.ani_pos = 0
        self.ani_max = len(self.ani) - 1
        self.img = pygame.image.load(self.ani[0])

        self.update(0)

    def update(self, pos):
        if pos >= 0:
            self.ani_pos = pos
            self.img = pygame.image.load(self.ani[self.ani_pos])
        screen.blit(self.img, (self.x, self.y))

character1 = character(50, 50, "img_sm/animal_alphabet_*.png")
character2 = character(50, 250, "img_sm/pic_*.png")
pos = 0

def calculate_pos(event):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    if event.type == KEYUP:
        if event.key == K_ESCAPE:
            sys.exit()
        return -1
    elif event.type == KEYDOWN:
        char = chr(event.key)
        if char in alphabets:
            return alphabets.index(char)
    return -1

while True:
    screen.fill((255, 255, 255))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pos = calculate_pos(event)

    character1.update(pos)
    character2.update(pos)

    pygame.display.update()


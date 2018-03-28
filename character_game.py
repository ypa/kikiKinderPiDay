#!/usr/bin/env python

import pygame, sys, glob
from pygame import *

HEIGHT = 800
WIDTH = 1000

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()


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
        SCREEN.blit(self.img, (self.x, self.y))


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


def main_loop():
    character1 = character(50, 50, "imgs/animal_alphabet_*.png")
    character2 = character(50, 250, "imgs/pic_*.png")
    pos = 0

    while True:
        SCREEN.fill((255, 255, 255))
        CLOCK.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pos = calculate_pos(event)

        character1.update(pos)
        character2.update(pos)

        pygame.display.update()

if __name__ == '__main__':
    main_loop()

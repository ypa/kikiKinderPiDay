import pygame
import os
from os.path import dirname, abspath, join

_image_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        image = pygame.image.load(path)
        _image_library[path] = image
    return image



class NamePad(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        self.done = False
        self.clock = pygame.time.Clock()

    def get_image_path(self, name):
        return join(dirname(abspath(__file__)), 'imgs', '{}.png'.format(name))

    def run(self):

        while not self.done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            self.fill_kobe()
            self.clock.tick(60)

    def fill_kobe(self):
        self.screen.fill((255, 255, 255))
        path = self.get_image_path('kobe')
        kobe = get_image(path)
        self.screen.blit(kobe, (20, 20))
        pygame.display.flip()


if __name__ == '__main__':
    pad = NamePad()
    pad.run()

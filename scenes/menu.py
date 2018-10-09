# coding: utf-8
# Konstantyn Davidenko
import os
import random

import pygame
from buttons import MoveButton
from scenes.base import SceneBase
from scenes.level1 import Level1

BACKGROUND = 'media/backgrounds'


def get_background():
    files = os.listdir(BACKGROUND)
    f_name = random.choice(files)
    return os.path.join(BACKGROUND, f_name)


class MainScene(SceneBase):
    """ Welcome screen of the game, the first one to be loaded."""

    def __init__(self, director):
        super().__init__(director)
        self.dir = director
        self.background_image = pygame.image.load(get_background())
        self.objects = []
        self.button_handler = []
        b = MoveButton(100, 100, 300, 50, 'test', 0, self.new_game)
        self.button_handler.append(b.handle_mouse_event)
        self.objects.append(b)

    def on_event(self, event):
        if event.type in (pygame.MOUSEBUTTONDOWN,
                          pygame.MOUSEBUTTONUP,
                          pygame.MOUSEMOTION):
            for handler in self.button_handler:
                handler(event.type, event.pos)

    def on_update(self):
        for o in self.objects:
            o.update()

    def on_draw(self, surface):
        surface.blit(self.background_image, (0, 0))
        for o in self.objects:
            o.draw(surface)

    def new_game(self, button):
        print('clicked')
        self.dir.change_scene(Level1(self.dir))

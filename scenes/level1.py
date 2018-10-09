# coding: utf-8
# Konstantyn Davidenko

import pygame

from calendar import MyCalendar
from scenes.base import SceneBase
from scenes.status_bar import StatusBar

BACKGROUND = 'scenes/level1/background.jpg'


class Level1(SceneBase):
    """ Welcome screen of the game, the first one to be loaded."""

    def __init__(self, director):
        super().__init__(director)
        self.background_image = pygame.image.load(BACKGROUND)
        self.objects = []
        self.button_handler = []
        self.time_run = 0
        self.cur_cycle = 0
        self.speed = 100
        self.calendar = MyCalendar()
        self.status_bar = StatusBar(director, (950, 150))

    def on_event(self, event):
        if event.type in (pygame.MOUSEBUTTONDOWN,
                          pygame.MOUSEBUTTONUP,
                          pygame.MOUSEMOTION):
            for handler in self.button_handler:
                handler(event.type, event.pos)

    def on_update(self):
        for o in self.objects:
            o.update()

        if self.time_run:
            self.cur_cycle += 1
            if self.cur_cycle % self.speed == 0:
                self.calendar.increment_date()
                self.calendar.print_date()

    def on_draw(self, surface):
        surface.blit(self.background_image, (0, 150))
        self.status_bar.on_draw(surface)

        for o in self.objects:
            o.draw(surface)

    def new_game(self, button):
        print('clicked')
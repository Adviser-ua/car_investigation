# coding: utf-8
# Konstantyn Davidenko
import pygame
import sys
import os
from collections import defaultdict
import random

from buttons import Button, MoveButton
from calendar import MyCalendar
from scenes.menu import MainScene

GAME_WIDTH = 1200
GAME_HEIGHT = 800
BACKGROUND = 'media/backgrounds'
CAPTION = 'Cars'
FRAME = 30
START_DATE = 0
SPEEDS = [100, 200, 300]


def get_background():
    files = os.listdir(BACKGROUND)
    f_name = random.choice(files)
    return os.path.join(BACKGROUND, f_name)


class Game:
    def __init__(self):
        self.calendar = MyCalendar()
        self.speed = SPEEDS[0]
        self.background_image = pygame.image.load(get_background())
        self.frame_rate = FRAME
        self.game_over = False
        self.objects = []
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        self.news = []
        self.time_ran = False

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        cur_cycle = 0
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
            if self.time_ran:
                cur_cycle += 1
                if cur_cycle % self.speed == 0:
                    self.calendar.increment_date()
                    self.calendar.print_date()



if __name__ == '__main__':
    game = Game()
    game.run()

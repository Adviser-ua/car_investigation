# coding: utf-8
# Konstantyn Davidenko
from time import sleep

import pygame

from game_object import GameObject
from text_object import TextObject
# import config as c
import colors

BUTTON_NORMAL_BACK_COLOR = colors.LIGHTBLUE
BUTTON_HOVER_BACK_COLOR = colors.ORANGE2
BUTTON_PRESSED_BACK_COLOR = colors.GREEN2

BUTTON_TEXT_COLOR = colors.BLACK
FONT_NAME = 'Arial'
FONT_SIZE = 20


class Button(GameObject):
    def __init__(self, x, y, w, h, text, on_click=lambda x: None, padding=0):
        super().__init__(x, y, w, h)
        self.state = 'normal'
        self.on_click = on_click

        self.text = TextObject(x + padding, y + padding, lambda: text, BUTTON_TEXT_COLOR, FONT_NAME, FONT_SIZE)

    @property
    def back_color(self):
        return dict(normal=BUTTON_NORMAL_BACK_COLOR,
                    hover=BUTTON_HOVER_BACK_COLOR,
                    pressed=BUTTON_PRESSED_BACK_COLOR
                    )[self.state]

    def draw(self, surface):
        pygame.draw.rect(surface, self.back_color, self.bounds)
        self.text.draw(surface, centralized=True)

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)

    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'

    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.state = 'pressed'

    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'


class MoveButton(Button):
    def __init__(self, x, y, w, h, text, init_pos_y=0, on_click=lambda x: None):
        self.y = y
        self.h = h
        super().__init__(x, init_pos_y, w, h / 2, text, on_click)

    def update(self):
        if self.bounds.y <= self.y:
            self.move(0, 50)
            self.text.pos = (self.bounds.x + self.width / 2, self.bounds.y + self.height / 2)
        else:
            self.bounds.height = self.h

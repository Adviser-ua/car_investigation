# coding: utf-8
# Konstantyn Davidenko

# -*- encoding: utf-8 -*-

# Modules
import os
import random
import sys
from collections import defaultdict

import pygame

GAME_WIDTH = 950
GAME_HEIGHT = 700

FRAME_RATE = 30


class Director:
    """Represents the main object of the game.

    The Director object keeps the game on, and takes care of updating it,
    drawing it and propagate events.

    This object must be used with Scene objects that are defined later."""

    def __init__(self):
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

        pygame.display.set_caption("Game Name")
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

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
            self.scene.on_event(event)

    def loop(self):
        "Main game loop."

        while not self.quit_flag:

            time = self.clock.tick(60)
            self.handle_events()

            # # Detect events
            # self.scene.on_event()

            # Update scene
            self.scene.on_update()

            # Draw the screen
            self.scene.on_draw(self.screen)
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(FRAME_RATE)

    def change_scene(self, scene):
        "Changes the current scene."
        self.scene = scene

    def quit(self):
        self.quit_flag = True
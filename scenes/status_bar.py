# coding: utf-8
# Konstantyn Davidenko
from colors import COLDGREY, BLUE2
from pygame.surface import Surface


class StatusBar(Surface):
    def __init__(self, dir, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dir = dir

    def on_draw(self, surface):
        self.fill(BLUE2)
        self.blit(surface, (0, 0))

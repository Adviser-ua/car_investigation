# coding: utf-8
# Konstantyn Davidenko

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modules
import pygame
import director
from scenes.menu import MainScene


def main():
    dir = director.Director()
    scene = MainScene(dir)
    dir.change_scene(scene)
    dir.loop()


if __name__ == '__main__':
    pygame.init()
    main()
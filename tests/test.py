import os
os.chdir(os.path.dirname(__file__))

import pygame
import time
import math
import sys
import gc
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            break

        keys = pygame.key.get_pressed()

        if keys[K_UP]:
            print("向上键被按下")
            running = False
        if keys[K_DOWN]:
            print("向下键被按下")
        if keys[K_LEFT]:
            print("向左键被按下")
        if keys[K_RIGHT]:
            print("向右键被按下")

    # print(pygame.key.name())
import os
os.chdir(os.path.dirname(__file__))

import pygame
import time
import math
import sys
import gc
from Objc import Objects as obj
from VGLN import Constant as con
from pygame.locals import *

pygame.init()

wd = pygame.display.set_mode(con.DW_SIZ)
wd.fill((0, 200, 0))

padpath = '../pic/panda1.png'
walpath = '../pic/wall1.png'

pad = obj(padpath)
wal = obj(walpath)

while True:
    for EVENT in pygame.event.get():
        if EVENT.type == QUIT:
            pygame.quit()
            sys.exit()

    for ioi in con.Wal_x:
        wal.setinfo([ioi, 0], con.WAL_SIZ)
        wal.show(wd)
    pad.setinfo([34-12, 0], con.PAD_SIZ)
    pad.show(wd)
    
    #
    pygame.display.update()

    # gc.collect()
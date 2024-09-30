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

padpath = '../pic/panda1.png'
walpath = '../pic/wall1.png'

pad = obj(padpath)
wal = obj(walpath)

ddd = False
uuu = False
rrr = False
lll = False

pad_y = 0
tempnum = 0
udspeed = 50

while True:
    for EVENT in pygame.event.get():
        if EVENT.type == QUIT:
            pygame.quit()
            sys.exit()
        elif EVENT.type == KEYDOWN:
            key_name = pygame.key.name(EVENT.key)
            # print("键盘按下：", EVENT.key, "对应的键名：", key_name)
            match key_name:
                case 'down':
                    ddd = True
                case 'up':
                    uuu = True
                case 'right':
                    rrr = True
                case 'left':
                    lll = True
                case _:
                    pass
        elif EVENT.type == KEYUP:
            key_name = pygame.key.name(EVENT.key)
            # print("键盘按下：", EVENT.key, "对应的键名：", key_name)
            match key_name:
                case 'down':
                    ddd = False
                case 'up':
                    uuu = False
                case 'right':
                    rrr = False
                case 'left':
                    lll = False
                case _:
                    pass


    wd.fill((0, 200, 0))

    for ioi in con.Wal_x:
        wal.setinfo([ioi, 0], con.WAL_SIZ)
        wal.show(wd)
    
    if ddd:
        tempnum += 1
        if tempnum >= udspeed:
            tempnum = 0
            pad_y += 1
            print(+1)
    if uuu:
        tempnum += 1
        if tempnum >= udspeed:
            tempnum = 0
            pad_y -= 1
            print(-1)
        
    pad.setinfo([34-12, pad_y], con.PAD_SIZ)
    pad.show(wd)
    
    #
    pygame.display.update()

    # gc.collect()
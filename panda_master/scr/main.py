import os
os.chdir(os.path.dirname(__file__))

import pygame
import math
import sys
import gc
import random
from Objc import Objects as obj
from VGLN import Constant as con
from pygame.locals import *
from ComputeFunc import ComputeFunc as cf

pygame.init()

# 建立窗口
wd = pygame.display.set_mode(con.DW_SIZ)

# 建立计算模组
computer = cf()

# 图片资源路径
padpath = '../pic/panda1.png'
walpath = '../pic/wall1.png'
oospath = ['../pic/Oor.png', 
           '../pic/Oob.png', 
           '../pic/Oog.png', 
           '../pic/Ooo.png',]

ddd = uuu = rrr = lll = False

pady, oosy0 = 0, con.DW_SIZ[1]    # 初始化panda和oos y位置坐标
pad_cy_temp = 0 # panda按键运动临界临时字
oos_cy_temp = 0 # oos自运动临界临时字
add_oo_temp = 0 # oo生成临界临时字
speedpad = 20   # panda运动速度(-)
speedoos = 200   # oos运动速度(-)
speedadd = 17000 # oo的生成速度(-)

# 构造可用的x位置坐标
ndvo_pad, ndvo_oos = 5, 3
rl_pad = computer.RightLeft_on_wall(con.PAD_SIZ[0], ndvo_pad)
rl_oos = computer.RightLeft_on_wall(con.OOO_SIZ[0], ndvo_oos)

pad = obj(padpath)  # 初始化panda
wal = obj(walpath)  # 初始化竹子
oos, oosxs, oosys = [], [], []

def addOo():
    tempoo = obj(random.choice(oospath))
    ooxindex = random.randint(0, len(rl_oos)-1)
    tempoo.setinfo([rl_oos[ooxindex], oosy0], con.OOO_SIZ)
    if ooxindex%2 != 0:
        tempoo.trun_x()
    oos.append(tempoo)
    oosys.append(oosy0)
    oosxs.append(rl_oos[ooxindex])
    print('the number of oos is' + ' ' + str(len(oos)))
    del tempoo


padxindex = 0  # panda的x位置索引

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
            # up down right left按键判断
            match key_name:
                case 'down':
                    ddd = False
                case 'up':
                    uuu = False
                case 'right':
                    pass
                    rrr = False
                case 'left':
                    pass
                    lll = False
                case _:
                    pass

    # 背景更新显示
    wd.fill((0, 200, 0))

    # 背景竹子显示更新
    for ioi in con.Wal_x:
        wal.setinfo([ioi, 0], con.WAL_SIZ)
        wal.show(wd)
    
    # 按键控制panda位置判断
    if ddd:
        pad_cy_temp += 1
        if pad_cy_temp >= speedpad and pady < con.WAL_SIZ[1]-con.PAD_SIZ[1]:
            pad_cy_temp = 0
            pady += 1
    if uuu:
        pad_cy_temp += 1
        if pad_cy_temp >= speedpad and pady > 0:
            pad_cy_temp = 0
            pady -= 1
    if rrr:
        rrr = False
        if padxindex < len(rl_pad)-1:
            padxindex += 1
            pad.trun_x()
    if lll:
        lll = False
        if padxindex > 0:
            padxindex -= 1
            pad.trun_x()

    # panda位置更新及显示
    padx = rl_pad[padxindex]
    pad.setinfo([padx, pady], con.PAD_SIZ)
    pad.show(wd)

    # oo生成
    add_oo_temp += 1
    if add_oo_temp >= speedadd:
        add_oo_temp = 0
        addOo()

    # oos自运动y位置更新及显示
    if len(oos) > 0:
        oos_cy_temp += 1
        if oos[0].rect.y > oosy0+10 or oos[0].rect.y < -10:
            oos.pop(0)
        if oos_cy_temp >= speedoos: # 设置出界判断(maybe)
            oos_cy_temp = 0
            for joj in range(len(oos)):
                oos[joj].setinfo([oos[joj].rect.x, oos[joj].rect.y-1])
        for kok in range(len(oos)):
            oos[kok].show(wd)
    

    pygame.display.update()

    # gc.collect()

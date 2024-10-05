import os
os.chdir(os.path.dirname(__file__))

import pygame
import math
import sys
import gc
import random
from Objc import oneObject as obj
from Objcs import Objects as objs
from VGLN import Constant as con
from pygame.locals import *
from ComputeFunc import ComputeFunc as cf

pygame.init()

# 建立窗口
wd = pygame.display.set_mode(con.WD_SIZ)

# 建立计算模组
computer = cf()

# 图片资源路径
padpath = ['../pic/panda1.png', 
           '../pic/panda2.png', 
           '../pic/panda3.png', 
           '../pic/panda4.png', ]
walpath = '../pic/wall1.png'
oospath = ['../pic/Oor.png', 
           '../pic/Oob.png', 
           '../pic/Oog.png', 
           '../pic/Ooo.png',]

ddd = uuu = rrr = lll = False
oddd= ddd   # 控制panda图片资源变化
padlife = True

pady, oosy0 = 0, con.WD_SIZ[1]    # 初始化panda和oos y位置坐标
pad_cy_temp = 0 # panda按键运动临界临时字
oos_cy_temp = 0 # oos自运动临界临时字
doo_cy_temp = 0 # 阵亡oos下落运动临界临时字
add_oo_temp = 0 # oo生成临界临时字
c_addoospeed_temp = 0 # 加快oo的生成速度的临界临时字
speedpad = 20   # panda运动速度(-)
speedoos = 200   # oos运动速度(-)
speeddoo = speedpad-5 # doo下落速度(-)
speedadd = 17000 # oo的生成速度(-)
addoospeed = 200 # 加快oo生成速度的速度(-)

# 构造可用的x位置坐标
ndvo_pad, ndvo_oos = 5, 3
rl_pad = computer.RightLeft_on_wall(con.PAD_SIZ[0], ndvo_pad)
rl_oos = computer.RightLeft_on_wall(con.OOO_SIZ[0], ndvo_oos)

pad = obj(padpath[0])  # 初始化panda
wal = obj(walpath)  # 初始化竹子
oos, oosxs, oosys, deadoos, doosxs, doosys = [], [], [], [], [], []

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
    print('the number of deadoos is ' + str(len(deadoos)))
    del tempoo

padxindex = 0  # panda的x位置索引

while True:
    for EVENT in pygame.event.get():
        # 点击退出
        if EVENT.type == QUIT:
            pygame.quit()
            sys.exit()
        
        # up down right left按键判断
        elif EVENT.type == KEYDOWN:
            key_name = pygame.key.name(EVENT.key)
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
        if pad_cy_temp >= speedpad: # and pady < con.WAL_SIZ[1]-con.PAD_SIZ[1]:
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

    # panda击杀模式判断
    if pady >= con.WAL_SIZ[1]-con.PAD_SIZ[1]:
        ddd = False
    if oddd != ddd:
        pad.cpic(padpath[(0 if padxindex%2 == 0 else 1) if not ddd else (2 if padxindex%2 == 0 else 3)])
        oddd = ddd
    
    # panda位置更新及显示
    padx = rl_pad[padxindex]
    pad.setinfo([padx, pady], con.PAD_SIZ)
    pad.show(wd)

    # oo生成加速
    '''c_addoospeed_temp += 1
    if c_addoospeed_temp >= addoospeed:
        c_addoospeed_temp = 0
        if speedadd > 200:
            speedadd -= 100'''
    
    # oo生成
    add_oo_temp += 1
    if add_oo_temp >= speedadd:
        add_oo_temp = 0
        addOo()

    # oos自运动y位置更新及显示
    if len(oos) > 0:
        oos_cy_temp += 1
        if oos_cy_temp >= speedoos:     # 运动判断
            oos_cy_temp = 0
            objs.litre(oos)
        objs.if_out(oos, con.OOO_SIZ)   # Oos出界判断
        objs.all_show(oos, wd)          # 显示

    # doo下落运动y位置更新及显示    # _ # 同上
    if len(deadoos) > 0:
        doo_cy_temp += 1
        if doo_cy_temp >= speeddoo:
            doo_cy_temp = 0
            objs.fall_(deadoos)
        objs.if_out(deadoos, con.OOO_SIZ)
        objs.all_show(deadoos, wd)

    # 碰撞判断
    # if len(oos) > 0:
    for non in range(len(oos)):
        tempoo = oos[non]
        if pad.rect.colliderect(tempoo.rect):
            if ddd:
                deadoos.append(tempoo)
                oos.pop(non)
            else:
                padlife = False
            break
    
    if not padlife:
        print('you dead! ')
        sys.exit()

    pygame.display.update()
    # gc.collect()

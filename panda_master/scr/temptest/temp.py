import os
os.chdir(os.path.dirname(__file__))

import pygame
import sys
import gc
from pygame.locals import *

# 定义一些全局变量
x = 10
y = 20
z = 30

def load_globals():
    # 获取所有全局变量
    global_vars = globals()
    
    # 更新局部命名空间
    locals().update(global_vars)
    
    # 使用全局变量
    print(f"x: {x}, y: {y}, z: {z}")
    
load_globals()

# 输出应该是:
# x: 10, y: 20, z: 30
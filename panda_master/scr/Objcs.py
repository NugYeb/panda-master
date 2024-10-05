import pygame
from pygame.locals import *
from VGLN import Constant as con
# from Objc import oneObject as obj1

class Objects(pygame.sprite.Sprite):

    def __init__(self):
        pass

    def litre(objs:list):
        for i in range(len(objs)):
            objs[i].setinfo([objs[i].rect.x, objs[i].rect.y-1])


    def fall_(objs:list):
        for i in range(len(objs)):
            objs[i].setinfo([objs[i].rect.x, objs[i].rect.y+1])

    
    def if_out(objs:list, siz:tuple, bottom=con.WD_SIZ[1], rightl=con.WD_SIZ[0]):
        if objs[0].rect.y > bottom or objs[0].rect.y < -siz[1] or objs[0].rect.x > rightl or objs[0].rect.x < -siz[0]:
            objs.pop(0)


    def all_show(objs:list, wd):
        for j in objs:
            j.show(wd)
import pygame
from pygame.locals import *

class oneObject(pygame.sprite.Sprite):

    def __init__(self, picpath):
        self.path = picpath

        self.initimg()


    def setinfo(self, pos=[0,0], siz=None):
        self.siz = siz
        self.pos = pos
        self.csiz()
        self.cpos()


    def initimg(self):
        self.img = pygame.image.load(self.path)
        self.rect = self.img.get_rect()


    def trun_x(self):
        self.img = pygame.transform.flip(self.img, True, False)
    
    
    def csiz(self):
        if self.siz:
            self.img = pygame.transform.scale(self.img, self.siz)
            self.rect.w = self.siz[0]
            self.rect.h = self.siz[1]


    def cpos(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]


    def cpic(self, npath:str):
        # temprect = self.img.get_rect()
        self.img = pygame.image.load(npath)
        self.csiz()
        self.cpos()



    def show(self, wd):
        wd.blit(self.img, self.rect)
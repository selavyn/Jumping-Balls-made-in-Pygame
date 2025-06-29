import pygame
import random
from ground import *

class Ball:
    fallSpeed = 0.5
    Balls = []
    def new(self,x,y,radius):
        self.Balls.append([x,y,radius,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),0,20])

    def update(self,screen):
        for obj in self.Balls:
            pygame.draw.circle(screen, obj[3], (obj[0],obj[1]), obj[2])
            if obj[1]+obj[2] >= Ground.Y:
                obj[4]=0
                obj[4]-=obj[5]
                obj[5]-=0.5
            else:
                obj[4]+=self.fallSpeed
            obj[1]+=obj[4]

            if obj[5]<0:
                self.Balls.remove(obj)
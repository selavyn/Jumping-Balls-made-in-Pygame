import pygame
import random
from ground import *


class Ball:
    fallSpeed = 3000
    Balls = []
    Ghosts = []

    def new(self,x,y,radius):
        self.Balls.append([x,y,radius,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),0,80000])
        print("Creating Ball", len(self.Balls))

    def update(self,screen, trail, dt, fps):
        for obj in self.Ghosts:
            obj[3]-=dt*1000
            if obj[3]<0:
                obj[3]=0
            pygame.draw.circle(trail, (255,255,255,obj[3]), (obj[0],obj[1]), obj[2])
            if obj[3]==0:
                self.Ghosts.remove(obj)


        for obj in self.Balls:
            pygame.draw.circle(screen, obj[3], (obj[0],obj[1]), obj[2])
            if obj[1]+obj[2] >= Ground.Y:
                obj[4]=0
                obj[4]-=(dt*(fps/60))*obj[5]
                obj[5]-=dt*100

            else:
                obj[4]+=dt*self.fallSpeed
            obj[1]+=dt*obj[4]

            self.Ghosts.append([obj[0],obj[1],obj[2],255])

            if obj[5]<5:
                self.Balls.remove(obj)


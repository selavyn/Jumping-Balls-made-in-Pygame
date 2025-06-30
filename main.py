import time

import pygame
import random

from pygame.time import Clock

from ball import *
from ground import *
import threading



width, height = 1280,720
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Jumping Balls")
trail_surf = pygame.Surface((width, height), pygame.SRCALPHA)

running = True

#Ball.new(Ball,random.randint(15,1265),150,20)

clock = pygame.time.Clock()

dt = clock.get_rawtime()

pygame.font.init()

font = pygame.font.SysFont("Comic Sans MS", 30)

ballTimer = 1

maxBalls = 30

for i in range(0,1280,100):
    Ball.new(Ball,i,i/3,25)
while running:
    dt = clock.get_time()/1000
    clock.tick(144)
    screen.fill((0,0,0))
    screen.blit(trail_surf, (0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event)
                for obj in Ball.Balls:
                    obj[4]=0
                    obj[4]-=(dt*(clock.get_fps()/60))*obj[5]
                    obj[5]-=dt*100


    ballTimer+=dt
    """if ballTimer>=random.randint(1,4):
        if len(Ball.Balls)+1<=maxBalls:
            Ball.new(Ball,random.randint(15,1265),150,random.randint(1,50))
        ballTimer=0"""



    #maxBalls = clock.get_fps()
    fps_text = font.render(str(clock.get_fps()), True, (255,255,255))
    #screen.blit(fps_text, (0,0))

    Ground.update(Ground, screen, width)
    Ball.update(Ball, screen, trail_surf, dt, clock.get_fps())


    pygame.display.update()
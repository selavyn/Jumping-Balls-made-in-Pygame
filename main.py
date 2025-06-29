import pygame
import random
from ball import *
from ground import *
import threading



width, height = 1280,720
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Jumping Balls")

running = True

#Ball.new(Ball,random.randint(15,1265),150,20)

clock = pygame.time.Clock()

ballTimer = 1

while running:

    screen.fill((0,0,0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            exit(0)

    ballTimer+=clock.get_time()/1000
    if ballTimer>=0.5:
        Ball.new(Ball,random.randint(15,1265),150,20)
        ballTimer=0

    Ground.update(Ground, screen, width)
    Ball.update(Ball, screen)

    clock.tick(60)
    pygame.display.update()
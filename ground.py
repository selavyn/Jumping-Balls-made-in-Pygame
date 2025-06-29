import pygame

class Ground:
    Y=600

    def update(self, screen, width):
        pygame.draw.line(screen, (255,255,255), (0,self.Y), (width,self.Y), 5)
import pygame
from pygame.locals import *

redColor   = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor  = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
grayColor  = pygame.Color(180,180,180)
blackColor = pygame.Color(0,0,0)

BoardPixel = ( 20 + 8*60 + 20, 20 + 8*60 + 20)
class Problem(object):
    def __init__(self, fen, surface):
        self.fen = fen
        self.surface = surface
        
    def update(self):
        for i in range(0,9):
            for j in range(0,9):
                rectColor = whiteColor
                if 1 == (i+j)%2:
                    rectColor = grayColor
                if i==8 or j==8:
                    rectColor = blackColor
                pygame.draw.rect(self.surface, rectColor, 
                                 ( 20+i*60, 20+j*60, 20+(i+1)*60, 20+(j+1)*60))
                    
        pygame.draw.rect(self.surface, blackColor, (0,0, 520,20))
        pygame.draw.rect(self.surface, blackColor, (0,0, 20,520))
        pygame.draw.rect(self.surface, blackColor, (520,520, 500,0))
        pygame.draw.rect(self.surface, blackColor, (520,520, 0,500))

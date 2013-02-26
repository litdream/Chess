#!/usr/bin/env python

import os
import sys
import pygame
from pygame.locals import *
from GameGraphic import *

if __name__ == '__main__':
    datafile = sys.argv[1]
    if not os.path.exists(datafile):
        print >>sys.stderr, "Data file NOT exists: %s" % datafile
        sys.exit(1)

    pygame.init()
    fpsClock = pygame.time.Clock()
    surface = pygame.display.set_mode( BoardPixel )
    
    problem = Problem('r1b2rk1/p1q1n1pp/3b1pn1/1Bp5/4P3/2N1BN1P/PPP2PP1/R2Q1RK1 w KQkq - 1 2', surface)
    while True:
        surface.fill(blackColor)
        problem.update()

        surface.blit(surface, (0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        pygame.display.update()
        fpsClock.tick(10)

from time import time
import pygame
from pygame import gfxdraw
from tqdm import tqdm
import math
import time
import numpy as np
from numba import njit

pygame.init()
win = pygame.display.set_mode((500, 500))
surface = pygame.Surface((500, 500),pygame.SRCALPHA,32)

I = (-1) ** .5
maxiter = 32
maxiter_255 = 255 / maxiter
ITER = maxiter
palette = [
    (
        int(255 * math.sin(i / 50.0 + 1.0) ** 2),
        int(255 * math.sin(i / 50.0 + 0.5) ** 2),
        int(255 * math.sin(i / 50.0 + 1.7) ** 2)
    ) for i in range(ITER - 1)
]
palette.append((0, 0, 0))

@njit(fastmath=True)
def f(z, c):
    return z ** 2 + c

def mandelbrot(x, y, scale):
    win.fill((0, 0, 0))
    j_list = [ ((j / scale + y) / 125 - 2) for j in range(500)]
    for i in range(500):
        i0 = (i / scale + x) / 125 - 2
        iteration =0
        for j in range(500):
            #c = i0 + j_list[j]
            z = complex(i0,j_list[j])
            c=z
            for depth in range(maxiter):
                # p = math.sqrt(pow(j-0.25,2) + i**2)
                # angl = math.atan2(i,j-0.25)
                # pc= 0.5 -(0.5*math.cos(angl))
                # if p <= pc:
                #   depth = maxiter -1
                #  break
                if abs(z) > 2:
                    iteration = depth
                    break
                z = f(z, c)
                iteration =depth
            #c = maxiter_255
            gfxdraw.pixel(win, i, j, palette[iteration])
        pygame.display.update()


class Julia:
    c = complex(-0.8, .156)
    def __init__(self):
        """Constructor"""
        pass


    def julia(self, x, y, scale):
        time = pygame.time.get_ticks()/1000
        win.fill((0, 0, 0))
        j_list = [((j / scale + y) / 125 - 2) for j in range(500)]
        for i in range(500):
            i0 = (i / scale + x) / 125 - 2
            iteration = 0
            for j in range(500):
                # c = i0 + j_list[j]
                self.c =complex(0.5*math.cos(0.5*time),0.5*math.sin(0.5*time))
                z = complex(i0, j_list[j])
                for depth in range(maxiter):
                    # p = math.sqrt(pow(j-0.25,2) + i**2)
                    # angl = math.atan2(i,j-0.25)
                    # pc= 0.5 -(0.5*math.cos(angl))
                    # if p <= pc:
                    #   depth = maxiter -1
                    #  break
                    if abs(z) > 2:
                        iteration = depth
                        break
                    z = f(z, self.c)
                    iteration = depth
                # c = maxiter_255
                gfxdraw.pixel(win, i, j, palette[iteration])
            pygame.display.update()


x, y, scale = 0, 0, 1
julia = Julia()

julia.julia(x, y, scale)
NextMove = pygame.time.get_ticks() + 2000

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONUP:
            if ev.button == 1:
                x0, y0 = ev.pos
                x += (x0) / scale
                y += (y0) / scale
                scale *= 2
                mandelbrot(x, y, scale)
            if ev.button == 3:
                x0, y0 = ev.pos
                x += (x0 ) / scale
                y += (y0) / scale
                scale /= 2
                mandelbrot(x, y, scale)
    CurrentTime = pygame.time.get_ticks()
    if CurrentTime >= NextMove:
        NextMove = pygame.time.get_ticks() + 2000
        julia.julia(x,y,scale)

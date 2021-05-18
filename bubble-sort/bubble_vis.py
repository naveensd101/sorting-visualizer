import random
import pygame
import sys
import time

WIDTH = 500
HEIGHT = 500
NUM = 50

WHITE = (225,225,225)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

h = []
for i in range(NUM):
    h.append(int((i + 1) * HEIGHT / NUM))
random.shuffle(h)

x = 0
y = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

for k in enumerate(h):
    Rect = [int(k[0] * WIDTH/NUM),int(HEIGHT - k[1]),int(WIDTH/NUM),int(k[1])]
    pygame.draw.rect(screen,RED,Rect)
    pygame.display.update()
time.sleep(1)

for i in range(NUM):
    for j in range(NUM - i - 1):
        a = h[j]
        b = h[j + 1]

        Rect = [int(j * WIDTH/NUM),int(HEIGHT - h[j]),int(WIDTH/NUM),int(h[j])]
        Rect_ = [int(j* WIDTH/NUM),0,int (WIDTH/NUM),HEIGHT]
        pygame.draw.rect(screen,BLACK,Rect_)
        pygame.draw.rect(screen,WHITE,Rect)
        pygame.display.update()

        if (a > b):
            temp = h[j]
            h[j] = h[j+1]
            h[j+1] = temp

            for k in enumerate(h):
                if k[0] == j+1 :
                    Rect = [int(k[0] * WIDTH/NUM),int(HEIGHT - k[1]),int(WIDTH/NUM),int(k[1])]
                    Rect_ = [int(k[0]* WIDTH/NUM),0,int (WIDTH/NUM),HEIGHT]
                    pygame.draw.rect(screen,BLACK,Rect_)
                    pygame.draw.rect(screen,WHITE,Rect)
                    pygame.display.update()

                elif k[0] > NUM - i- 1:
                    Rect = [int(k[0] * WIDTH/NUM),int(HEIGHT - k[1]),int(WIDTH/NUM),int(k[1])]
                    Rect_ = [int(k[0]* WIDTH/NUM),0,int (WIDTH/NUM),HEIGHT]
                    pygame.draw.rect(screen,BLACK,Rect_)
                    pygame.draw.rect(screen,BLUE,Rect)
                    pygame.display.update()

                else:
                    Rect = [int(k[0] * WIDTH/NUM),int(HEIGHT - k[1]),int(WIDTH/NUM),int(k[1])]
                    Rect_ = [int(k[0]* WIDTH/NUM),0,int (WIDTH/NUM),HEIGHT]
                    pygame.draw.rect(screen,BLACK,Rect_)
                    pygame.draw.rect(screen,RED,Rect)
                    pygame.display.update()

        clock.tick(24)

for k in enumerate(h):
    Rect = [int(k[0] * WIDTH/NUM),int(HEIGHT - k[1]),int(WIDTH/NUM),int(k[1])]
    pygame.draw.rect(screen,BLUE,Rect)
    pygame.display.update()

while True:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT ):
            sys.exit()
        if (event.type == pygame.KEYDOWN ):
            if(event.key == pygame.K_ESCAPE):
                sys.exit()

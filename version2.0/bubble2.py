#-------------------------------------------------------------------------------
#Favourite colours
#-------------------------------------------------------------------------------
orange = (95, 38, 33)
blue = (41, 66, 88)
magenta = (58, 14, 34)
green = (25, 49, 36)

#-------------------------------------------------------------------------------
#All imports
#-------------------------------------------------------------------------------
import pygame
import sys#for exit functions
import os#to set pygame window at one position
import random#for height generation

#-------------------------------------------------------------------------------
#settings of pygame display screen
#-------------------------------------------------------------------------------
scr = {
    'x' : 400 * 2,
    'y' : 300 * 2
}
screen = pygame.display.set_mode((scr['x'], scr['y']))
pygame.display.set_caption("Sorting Visualiser")
clock = pygame.time.Clock()

#-------------------------------------------------------------------------------
#List of heihts for bars and setting number of bars
#-------------------------------------------------------------------------------
heights = []#list to store all the heights
def devisors(n) :
    devis = []
    for i in range (1, n + 1) :
        if(n % i == 0) :
            devis.append(i)
    return devis

num = 20
for i in range(1, num + 1) :
    h = (scr['y'] / num) * i
    heights.append(h)
random.shuffle(heights)

#-------------------------------------------------------------------------------
#Everything of rectangle bars
#-------------------------------------------------------------------------------
class rectangle :
    def __init__(self, num = 1, pos = 0, height = 300):
        self.num = num#number of rectangles that will be displayed at once
        self.pos = pos#unique key for each rectangle, to identify position 0..(num - 1)
        self.height = height#height of each rectangle
        self.thicknes = scr['x'] / self.num
        self.x = self.pos * scr['x'] / self.num
        self.y = scr['y'] - self.height
        self.Rect_ = (self.x, self.y, self.thicknes, self.height)

    def drawRec(self, colour = blue):
        self.thicknes = scr['x'] / self.num
        self.x = self.pos * scr['x'] / self.num
        self.y = scr['y'] - self.height
        self.Rect_ = (self.x, self.y, self.thicknes, self.height)
        pygame.draw.rect(screen, colour, self.Rect_)
        pygame.display.update()
        clock.tick(24)

#-------------------------------------------------------------------------------
#setting up the bars with its position and height
#-------------------------------------------------------------------------------
list_of_rectangles = []
for i in range(num) :
    instance = rectangle(num = num, pos = i, height = heights[i])
    list_of_rectangles.append(instance)

#-------------------------------------------------------------------------------
#Displaying everything in pygame window
#-------------------------------------------------------------------------------
while True:#pygame loop to execute infinitely
    for event in pygame.event.get():#loop to exit anytime
        if(event.type == pygame.QUIT):
            sys.exit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_ESCAPE):
                sys.exit()

    for obj in list_of_rectangles :
        obj.drawRec()
    for obj in list_of_rectangles :
        obj.drawRec(colour = magenta)

#-------------------------------------------------------------------------------

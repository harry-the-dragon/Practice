import pygame
from math import pi
pygame.init()

screen = pygame.display.set_mode((100,100))
White = pygame.Color (255,255,255)
Red = pygame.Color (255,2,5)


#shape
size = (50,50)
points = [(25,0), (50,0), (25,50), (0,25)]

polygon = pygame.Surface(size)
pygame.draw.polygon (polygon, Red, points,10)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.blit(polygon, (25,25))
    pygame.display.update()





import pygame
import random
import math

pygame.init()

while True:
    for event in pygame.event.get():
        print(event)
        break
    screen_width = 500
    screen_height = 500

    screen = pygame.display.set_mode([screen_width, screen_height])
    screen.fill("forestgreen")

    pygame.draw.circle(screen,"black", (250,250),251)
    pygame.draw.circle(screen,"firebrick3", (250,250),250)
    pygame.draw.line(screen,"black",(250,0),(250,500))
    pygame.draw.line(screen,"black",(0,250),(500,250))
    pygame.display.flip()
    pygame.time.wait(1000)

    for i in range(10):
        x = random.randrange(screen_width)
        y = random.randrange(screen_height)

        distance_from_center = math.hypot(x-250, y-250)
        is_in_circle = distance_from_center <= screen_width/2

        if is_in_circle == True:
            pygame.draw.circle(screen, "yellow", (x,y),5)
            pygame.display.flip()
            pygame.time.wait(500)
        else:
            pygame.draw.circle(screen, "blue", (x,y),5)
            pygame.display.flip()
            pygame.time.wait(500)

    break

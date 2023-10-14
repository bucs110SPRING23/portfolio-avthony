import pygame
import random
import math

pygame.init()
pygame.font.init()
screen_width = 500
screen_height = 500

player1_score = 0
player2_score = 0

screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill("forestgreen")

pygame.draw.circle(screen,"black", (250,250),251)
pygame.draw.circle(screen,"firebrick3", (250,250),250)
pygame.draw.line(screen,"black",(250,0),(250,500))
pygame.draw.line(screen,"black",(0,250),(500,250))
pygame.display.flip()
pygame.time.wait(1000)



while True:
    for event in pygame.event.get():
        print(event)
    
    for i in range(10):
        x1 = random.randrange(screen_width)
        y1 = random.randrange(screen_height)
        x2 = random.randrange(screen_width)
        y2 = random.randrange(screen_height)

        distance_from_center1 = math.hypot(x1-250, y1-250)
        distance_from_center2 = math.hypot(x2-250, y2-250)
        is_in_circle1 = distance_from_center1 <= screen_width/2
        is_in_circle2 = distance_from_center2 <= screen_width/2

        if is_in_circle1 == True:
            pygame.draw.circle(screen, "yellow", (x1,y1),5)
            pygame.display.flip()
            player1_score = player1_score + 1
        else:
            pygame.draw.circle(screen, "blue", (x1,y1),5)
            pygame.display.flip()
        if is_in_circle2 == True:
            pygame.draw.circle(screen, "pink", (x2,y2),5)
            pygame.display.flip()
            pygame.time.wait(500)
            player2_score = player2_score + 1
        else:
            pygame.draw.circle(screen, "purple", (x2,y2),5)
            pygame.display.flip()
            pygame.time.wait(500)
        
    if player1_score == player2_score:
        font = pygame.font.Font(None, 48)
        text = font.render("The players tied!", True, "white")
        screen.blit(text, (250, 250))
        
    elif player1_score > player2_score:
        font = pygame.font.Font(None, 48)
        text = font.render("Player 1 wins!", True, "white")
        screen.blit(text, (250, 250))
        
    elif player1_score < player2_score:
        font = pygame.font.Font(None, 48)
        text = font.render("Player 2 wins!", True, "white")
        screen.blit(text, (100, 250))
    
    pygame.display.flip()
    pygame.time.wait(5000)
    
    break
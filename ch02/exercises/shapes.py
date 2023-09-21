import pygame

pygame.init()

while True:
    for event in pygame.event.get():
        print(event)
        break
    screen = pygame.display.set_mode()

    pygame.draw.circle(screen, "white", (750,700), 100)
    pygame.time.wait(5000)
    pygame.display.flip()

    pygame.draw.circle(screen, "white", (750,615), 75)
    pygame.time.wait(5000)
    pygame.display.flip()

    pygame.draw.circle(screen, "white", (750,540), 50)
    pygame.display.flip()
    pygame.time.wait(5000)

    break

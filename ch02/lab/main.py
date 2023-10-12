import turtle  # 1. import modules
import random
import pygame
import math

# Part A
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor("lightblue")

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")

michelangelo.up()  # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

# Race 1
race1_random = random.randrange(100)

michelangelo.forward(race1_random)

race1_random = random.randrange(100)

leonardo.forward(race1_random)

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

#Race 2

race2_random1 = random.randrange(20)
race2_random2 = random.randrange(20)

for i in range(10):
    michelangelo.forward(race2_random1)
    leonardo.forward(race2_random2)

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

window.exitonclick()

pygame.init()
window = pygame.display.set_mode()

while True:
    for event in pygame.event.get():
        pass
    
    points = []
    num_sides = int(input("enter the number of sides "))
    side_length = int(input(" enter the length of each side "))
    xpos = int(input("enter the top left x coordinate of the shape((0,0) is the top left corner) "))
    ypos = int(input("enter the the top left y coordinate of the shape "))

    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle*i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])

    pygame.draw.polygon(window,"green",points)
    pygame.display.flip()
    pygame.time.wait(5000)

    window.fill("black")
    pygame.display.flip()

    points = []




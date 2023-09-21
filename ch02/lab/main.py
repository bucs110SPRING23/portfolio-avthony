import turtle  # 1. import modules
import random

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

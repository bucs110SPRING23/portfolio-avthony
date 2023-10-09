import random
import math

number = random.randint(1,1000)
guess = 0
number_guesses = 0

while guess != number:
    guess = int(input("please enter a guess for the number: "))
    number_guesses += 1
    if number == guess:
        print("That's right!")
        break
    elif number < guess:
        print("too high")
    elif number > guess:
        print("too low")
        
print("It took you ", number_guesses, " guesses to get it right, the number was", number)
print("It should take you at most", 9, "guesses")


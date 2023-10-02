import random

number = random.randrange(1,11)

for i in range(3):
    guess = int(input("please enter a guess for the number: "))
    if number == guess:
        print("That's right!")
        break
    elif number < guess:
        print("too high")
    elif number > guess:
        print("too low")
        

import random

number_guess = random.randint(1, 100)
print("guess a number between 1 and 100")
guess = int(input("enter your guess: "))

while guess != number_guess:
    if guess > number_guess:
        print("too high")
        guess = int(input("enter your guess: "))
        (guess, number_guess)
    elif guess < number_guess:
        print("too low")
        guess = int(input("enter your guess: "))
print("you guessed it!")

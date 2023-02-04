import random

def guessing_game():
    number = random.randint(1, 10)
    guess = None
    tries = 0
    print("Welcome to the guessing game!")
    while guess != number:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess > number:
            print("Too high! Try again.")
            tries += 1
        elif guess < number:
            print("Too low! Try again.")
            tries += 1
    print("Congratulations, you guessed the number in", tries, "tries!")

guessing_game()

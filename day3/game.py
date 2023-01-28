import random

# Generate a random 3-digit number
answer = str(random.randint(100, 999))

# Initialize number of tries
tries = 0

while True:
    # Get user's guess
    guess = input("Guess a 3-digit number: ")

    # Check if guess is valid
    if not guess.isdigit() or len(guess) != 3:
        print("Invalid guess, please enter a 3-digit number.")
        continue

    # Increment number of tries
    tries += 1

    # Check for exact matches
    exact_matches = 0
    for i in range(3):
        if guess[i] == answer[i]:
            exact_matches += 1

    # Check for number matches
    number_matches = 0
    for i in range(3):
        if guess[i] in answer:
            number_matches += 1

    # Subtract exact matches from number matches
    number_matches -= exact_matches

    # Print number of exact and number matches
    print("Exact matches:", exact_matches)
    print("Number matches:", number_matches)

    # Check for win
    if guess == answer:
        print("Congratulations! You won in", tries, "tries!")
        break

import random

def play_hangman():
    word_list = ["python", "javascript", "computer", "science", "programming"]
    word = random.choice(word_list)
    word = word.upper()
    word_letters = set(word)
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    used_letters = set()
    word_guessed = set()
    tries = 6
    print("Let's play Hangman!")
    print("The word has", len(word), "letters.")
    while (len(word_letters) > 0) and tries > 0:
        print("You have", tries, "tries left.")
        if len(used_letters) > 0:
            print("Used letters: ", " ".join(used_letters))
        print("Word: ", " ".join(letter if letter in word_guessed else "_" for letter in word))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                word_guessed.add(user_letter)
            else:
                tries -= 1
        else:
            print("You already used that letter. Try again.")
    if tries == 0:
        print("You lost! The word was", word)
    else:
        print("Congratulations! You correctly guessed the word", word)

play_hangman()

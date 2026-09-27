import random

def play_hangman():
    words = ["python", "hangman", "computer", "keyboard", "program"]

    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")

    while attempts > 0:
        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("Word:", display)
        print("Attempts left:", attempts)

        if "_" not in display:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

    if attempts == 0:
        print("Game Over! The word was:", word)


if __name__ == "__main__":
    play_hangman()

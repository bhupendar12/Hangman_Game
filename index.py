import random

def hangman():         # Main function that runs the Hangman game
    
    words = ['orange', 'radish', 'hangman', 'programming']    # List of possible words
    word = random.choice(words)     # Randomly select a word from the list

    guessed_word = []           # Store letters guessed by the player

    attempts = 6               # Number of incorrect guesses allowed
    print('Welcome to Hangman')
    print('Try to guess the word letter by letter. You have 6 attempts')

    while attempts > 0:        # Continue until the player runs out of attempts

        # Display guessed letters and hide remaining letters with underscores
        display_word = ''.join(
            [letter if letter in guessed_word else '_' for letter in word]
        )

        print(display_word)

        # Check if the player has guessed the entire word
        if display_word == word:
            print('You won! The word was:', word)
            break

        # Take user input and convert it to lowercase
        guess = input('Guess a letter: ').lower()

        # Reduce attempts if the guessed letter is not in the word
        if guess not in word:
            attempts -= 1
            print(f'Wrong guess! You have {attempts} attempts left')

        # Store the guessed letter
        guessed_word.append(guess)

    # Game over message if all attempts are used
    if attempts == 0:
        print('You lost! The word was:', word)
        print('Better luck next time!')

hangman()
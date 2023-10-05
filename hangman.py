import random
from listofwords import list_of_words as imported_words


def get_word():
    word = random.choice(imported_words)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6
    print("Let's play Hangman!")
    print(word_completion)
    print("\n")
    while not guessed and attempts > 0:
        print(hangman_display(attempts))
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good job!", guess, "is in the word!")
                guessed_letters.append(guess)
                list_of_words = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    list_of_words[index] = guess
                    word_completion = "".join(list_of_words)
                    if "_" not in word_completion:
                        guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

    else:
        print("Not a valid guess.")
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations, player. You guessed the correct word. You win!")
    else:
        print("Sorry, your tries have ran out. The correct word was " + word +
              ". Better luck next time")
        print(hangman_display(attempts))


def hangman_display(attempts):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[attempts]


def main():
    word = get_word()
    play(word)
    while input("Do you want to play again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""This program implements a variation of the classic hangman game.

This project comes from MIT’s 6.0001 Introduction to Computer Science and
Programming in Python course and was released under the CC BY-NC-SA license.
It is meant to be challenging, but also fun. Relax, enjoy, and, if worse comes
to worse, remember that you do not have to complete the project to get a
passing grade on it
"""


# start of helper code
# -----------------------------------
# You don't need to understand the helper code below but you will have to know
# how to use the functions so be sure to read the provided comments!

import random
import string
import pathlib


WORDLIST_FILENAME = "words.txt"


def load_words(argo, hello, python):
    """Return a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may take a while to
    finish.

    Returns:
        list: a list of strings
    """
    print("Loading word list from file...")

    # file is the fully qualified path to a file on disk
    file = pathlib.Path(pathlib.Path(__file__).parent) / WORDLIST_FILENAME

    # in_file represents a file on disk, we can use this to read the file's
    # contents
    in_file = open(file, "r")

    # line is the string read from in_file
    line = in_file.readline()

    # word_list is a list of strings made by splitting line on space characters
    word_list = line.split()

    print(len(word_list), "words loaded.")

    return word_list


def choose_word(word_list):
    """Choose a random word from a list.

    Args:
        word_list (list): list of strings

    Returns:
        string: a random string from word_list
    """
    return random.choice(word_list)


# Load the list of words into the global variable WORDS so that it can be
# accessed from anywhere in the program
#WORDS = load_words()

# -----------------------------------
# end of helper code


def is_word_guessed(secret_word, letters_guessed):
    """Return whether or not the entire secret word has been guessed.

    Args:
        secret_word (string):  the word the user is guessing; assumes all
        letters are lowercase

        letters_guessed (list): a list of strings where each string is exactly
        one character (letter) that has already been guessed; assumes that all
        characters are lowercase

    Returns:
        boolean: True if all the letters of secret_word are in letters_guessed;
        False otherwise
    """
    def get_word():
        word = random.choice(word_list)
        return word.upper()

    def play(word):
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries=6
        print("Do you want to play hangman?")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

def get_guessed_word(secret_word, letters_guessed):
    """Build a string representing the word as the user has guessed it.

    Where the user has guessed a letter in the secret word, that letter should
    appear in the correct place in the returned string. Letters in the secret
    word that have not yet been guessed should be represented by a combination
    of an underscore-and-space ('_ ').

    Args:
        secret_word (string): the secret word the user is guessing

        letters_guessed (list): a list of strings where each string is exactly
        one character (letter) that has already been guessed; assumes that all
        characters are lowercase

    Returns:
        string: a string comprised of letters, underscores (_), and spaces
        representing the user's guess so far
    """



def get_available_letters(letters_guessed):
    """Build a sting containing all the still available letters.

    Available letters are those that have not yet been guessed.

    Args:
        letters_guessed (list): a list of strings where each string is exactly
        one character (letter) that has already been guessed; assumes that all
        characters are lowercase

    Returns:
        string: a string comprised of all the remaining letters which have not
        yet been guessed
    """
    while not guessed and tries > 0:
        guess = input("please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("the letter has already been guessed", guess)
            elif guess not in word:
                print(guess, "not in the word:")
                tries -= 1
                guessed_letters.append(gues)
            else:
                print("nicely done,", guess, "is the word.")
                word_as_list = list(word_completion)
                indicies = [i for i, letter in enumerate(word) if letter == guess]
                for index in indicies:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you have already guessed this word", guess)
            elif guess != word:
                print(guess, "this is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word


        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congradulations! you guessed the word correctly")
    else:
        print("Sorry, you have no more tries left. The word was" + word + "good luck next time")




def hangman(secret_word):
    """Start an interactive game of Hangman.

    * At the start of the game, the computer selects a word at random from the
      list of available words proficed in words.txt.

    * The user starts with a number of guesses equal to the length of the word
      plus one.

    * The user also starts the game with three warnings.

    * Let the user know how many letters the secret word contains and how many
      guesses they start with.

    * Before each round, display to the user how many guesses they have left
      as well as the letters that have not been guessed yet.

    * Ask the user to supply one guess per round, make sure to check that the
      user guesses a valid letter (not a number or other symbol).

    * The user should receive feedback immediately after each guess about
      whether their guess appears in the computer's word.

    * After each guess, display the partially guessed word - insert the letters
      the user has correctly guessed in the correct place(s) in the word and
      display an underscore followed by a space ("_ ") for all letters that
      have not yet been guessed.

    * Every time the user enters anything besides a letter (such as a number or
      symbol) or if they guess a letter they had previously guessed, they lose
      a warning. If the user has no more warnings remaining, they lose a guess
      a guess.


    Follows the other limitations detailed in the project write-up.

    Args:
        secret_word (string): the secret word to guess
    """
    # REPLACE THE "pass" STATEMENT BELOW WITH YOUR CODE
def main():
    word = get_word()
    play(word)
    while input("do you want to play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)



if __name__ == "__main__":
    main()

    ############################################################################
    # To test your is_word_guessed function uncomment the three lines below and
    # run the program. The function should return False given the values below.
    # Feel free to experiment with other values for secret_word and
    # letters_guessed.
    ############################################################################

    # secret_word = 'apple'
    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # print(is_word_guessed(secret_word, letters_guessed))

    ############################################################################
    # To test your get_guessed_word function uncomment the three lines below and
    # run the program. The function should return the string "_ pp_ e" given the
    # values below. Feel free to experiment with other values for secret_word
    # and letters_guessed.
    ############################################################################

    # secret_word = 'apple'
    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # print(get_guessed_word(secret_word, letters_guessed))
    # '_ pp_ e'

    ############################################################################
    # To test your get_available_letters function uncomment the three lines
    # below and run the program. The function should return the string
    # "abcdfghjlmnoqtuvwxyz" given the values below. Feel free to experiment
    # with other values for letters_guessed.
    ############################################################################

    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # print get_available_letters(letters_guessed)
    # abcdfghjlmnoqtuvwxyz

    ############################################################################
    # Now it is time to test your hangman function. Uncomment the two lines
    # below and run the program to play the game. Hint: You might want to pick
    # your own secret_word while you're testing. To do so, comment out the line:
    #
    # secret_word = choose_word(WORDS)
    #
    # and replace it with:
    #
    # secret_word = "secret"
    #
    # or any other word of your choosing. Be sure to replace the call to
    # choose_word and test the program again before submitting it.
    ############################################################################

    # secret_word = choose_word(WORDS)
    # hangman(secret_word)
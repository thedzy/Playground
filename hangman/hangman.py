#!/usr/bin/env python3

"""
Script:	hangman.py
Date:	2020-04-24

Platform: MacOS

Description:
A traditional hangman game.  Customisable hangman art, words, phrases, and dictionary

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2020, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Developer'

import argparse
import os
import random

import hangman_art


def main():
    # Initialise the valid character set to latin
    characters_valid = list('abcdefghijklmnopqrstuvwxyz')

    # Get the provided phrase/word to sue of pick
    if len(options.phrase) > 0:
        word = ' '.join(options.phrase)
    else:
        if options.word is None:
            # Load in dictionary file
            dictionary = options.dictionary.read()
            options.dictionary.close()

            # Get a new valid characters from dictionary, make hangman adaptable to other languages
            characters_valid.extend(set(dictionary.lower()))
            characters_valid = list(set(characters_valid))
            dictionary = dictionary.splitlines()

            # Take out any line breaks and sort the list for display
            characters_valid.remove('\n')
            characters_valid.sort()

            # Shuffle to get random words
            # Note: Using shuffle and not choice so that there cannot be a endless loop condition finding a word
            random.shuffle(dictionary)

            # Check if we are going to use a word longer than is in the dictionary
            dictionary_length_max = len(max(dictionary, key=len))
            if options.length_max > dictionary_length_max:
                print('Longest word in dictionary is {} characters, Setting new max'.format(dictionary_length_max))
                options.length_max = dictionary_length_max

            # Make sure min an max values cannot to opposite of each other
            if options.length_max < options.length_min:
                options.length_min = options.length_max

            if options.debug:
                print('Min', options.length_min, ', Max', options.length_max)

            # Loop through to find our first match and exit the loop if there is a problem
            for word in dictionary:
                if options.length_min <= len(word) <= options.length_max:
                    word = word
                    break
        else:
            word = options.word.lower()

    word = word.lower()

    # Initialise the guessing, with space already guessed
    guesses = [' ']
    guess = ' '

    # Initialise counters and limits
    errors_max = len(hangman_art.objects) - 1  # Maximum amount of errors allows, based on body part count
    errors = 0
    correct = 0
    character_count = len(set(word.replace(' ', '')))

    # Start puzzle
    while True:
        # Reset the screen to keep a fix position
        reset_screen()

        # Display guessed characters in the sorted order
        print('Guessed letters')
        for character in characters_valid:
            if character in guesses:
                print(character.upper(), end='')
            else:
                print(' ', end='')
        print()

        # Print the hangman
        print_man(errors)

        # Display the word with blanked out characters
        for character in word:
            if character in guesses:
                print(character.upper(), end='')
            else:
                print('_', end='')
        print()

        # Print out the results
        if errors >= errors_max or correct >= character_count or options.debug:
            print(word.upper())

        # Check if we won or lost
        if errors >= errors_max:
            print('You lose')
            exit()
        elif correct >= character_count:
            print('You win')
            exit()

        # Loop until we have a new character not used before
        while guess in guesses:
            # Get choice
            guess = input('\nLetter or complete puzzle? ')
            guess = guess.lower()

            # Do not accept empty answers
            if len(guess) == 0:
                guess = ' '
                break

            # If a single character is entered
            if len(guess) == 1:
                if guess not in characters_valid:
                    print('Letter {} is not in the dictionary'.format(guess))
                    guess = ' '
                    continue

                if guess in guesses:
                    print('You guessed the letter {} already'.format(guess.upper()))

            # If solving the puzzle
            if len(guess) > 1:
                print('Guessing {} to solve the puzzle'.format(guess))
                if guess == word:
                    correct = character_count
                    continue
                else:
                    errors = errors_max
                    continue

        # Do not append the guess if user tried to solve
        if len(guess) == 1:
            guesses.append(guess)

        # Keep score
        if guess in word:
            correct += 1
        else:
            errors += 1


def print_man(errors=0):
    """
    Print the hangman from the hangman_art file
    :param errors: (int) Error number
    :return: (void)
    """
    hangman_shaders = hangman_art.shaders
    hangman_objects = hangman_art.objects

    # Get the width and height dynamically
    height, width = 0, 0
    for hangman_object in hangman_objects:
        if height < len(hangman_object):
            height = len(hangman_object)
        for row in hangman_object:
            if width < len(row):
                width = len(row)

    for x in range(height):
        for y in range(width):
            value = 0
            for hangman_object in range(errors + 1):
                try:
                    value = max(hangman_objects[hangman_object][x][y], value)
                except IndexError:
                    pass
            print(hangman_shaders[value], end='')
        print()
    print()


def reset_screen(y_position=0, x_position=0):
    # Send an ansi clear
    print('\033[2J')
    # Set the cursor
    print('\033[{:d};{:d}H'.format(y_position, x_position))


if __name__ == '__main__':

    def parser_formatter(format_class, **kwargs):
        """
        Use a raw parser to use line breaks, etc
        :param format_class: (class) formatting class
        :param kwargs: (dict) kwargs for class
        :return: (class) formatting class
        """
        try:
            return lambda prog: format_class(prog, **kwargs)
        except TypeError:
            return format_class

    parser = argparse.ArgumentParser(description='A traditional hangman game.',
                                     formatter_class=parser_formatter(
                                         argparse.RawTextHelpFormatter,
                                         indent_increment=4, max_help_position=12, width=160))

    # Dictionary/word/phrase
    parser.add_argument('-d', '--dict', type=argparse.FileType('r'),
                        action='store', dest='dictionary',
                        default=os.path.join(os.path.dirname(__file__), 'collins_scrabble_words_2019.txt'),
                        help='Dictionary file to use'
                             '\nDefault: %(default)s')

    parser.add_argument('-w', '--word', type=str,
                        action='store', dest='word', default=None,
                        help='Word or phrase to use'
                             '\nDefault: Random selection from the dictionary')

    parser.add_argument('-p', '--phrase', type=str,
                        action='store', dest='phrase', default=[], nargs='+',
                        help='Word or phrase to use'
                             '\nDefault: Random word from the dictionary')

    # Word lengths when randomly generated
    parser.add_argument('-l', '--length', type=int,
                        action='store', dest='length', default=None,
                        help='Only a fixed length word is generated'
                             '\nNote: Overrides minimum and maximum values')

    parser.add_argument('-x', '--max', type=int,
                        action='store', dest='length_max', default=32,
                        help='Maximum word length generated'
                             '\nDefault: %(default)s')

    parser.add_argument('-m', '--min', type=int,
                        action='store', dest='length_min', default=1,
                        help='Minimum word length generated'
                             '\nDefault: %(default)s')

    # Testing and debugging
    parser.add_argument('--debug',
                        action='store_true', dest='debug', default=False,
                        help='Debug the program'
                             '\nDefault: %(default)s')

    options = parser.parse_args()

    if options.length is not None:
        options.length_min = options.length
        options.length_max = options.length

    if options.word and options.phrase:
        print('Word and phrase provided, using phrase')

    main()

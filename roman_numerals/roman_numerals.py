#!/usr/bin/env python3
"""
Script:	roman_numerals.py
Date:	2021-12-29	

Platform: macOS/Windows/Linux

Description:

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2021, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'
__description__ = """
    convert roman numerals
"""

import argparse
import logging


def main():
    # Setup logging
    logging.basicConfig(format='{message}', level=options.debug, style='{')

    # Enumerate values and letters
    roman = {
        'i': 1, 'I': 1000,
        'v': 5, 'V': 5000,
        'x': 10, 'X': 10000,
        'l': 50, 'L': 50000,
        'c': 100, 'C': 100000,
        'd': 500, 'D': 500000,
        'm': 1000, 'M': 1000000,
    }
    arabic = {
        1: ('i', 'iv',), 1000: ('I', 'IV',),
        5: ('v', 'vx',), 5000: ('V', 'VX',),
        10: ('x', 'xl',), 10000: ('X', 'XL',),
        50: ('l', 'lc',), 50000: ('L', 'LC',),
        100: ('c', 'cd',), 100000: ('C', 'CD',),
        500: ('d', 'dm',), 500000: ('D', 'DM',),
        1000: ('m', 'IV',), 1000000: ('M', 'MMMM',),
    }

    # If using underscore notation, just change it to case
    if options.roman_score:
        numerals = ''
        for index, character in enumerate(options.roman_score.lower()):
            if character == '_':
                continue
            elif options.roman_score.upper()[index - 1] == '_':
                numerals += character.upper()
            else:
                numerals += character.lower()
        numerals += numerals[-1] * 3
    elif options.roman_case:
        numerals = options.roman_case + options.roman_case[-1] * 3

    # If converting from roman numbers
    if options.roman_score or options.roman_case:
        logging.debug('Fom roman numerals')
        logging.debug(f'Converting: {numerals[:-3]}')

        number = 0
        for index, letter in enumerate(numerals[:-3]):
            value = roman[letter]
            logging.debug(f' Value compare: {value} > {roman[numerals[index + 1]]}')
            if value >= roman[numerals[index + 1]]:
                number += value
            else:
                number -= value
            logging.debug(f'Number: {number}')
        if options.roman_score:
            logging.info(f'{options.roman_score.upper()} -> {number}')
        elif options.roman_case:
            logging.info(f'{options.roman_case} -> {number}')

    # If converting from arabic/english numbers
    if options.arabic:
        print('From arabic numbers:')
        numerals = ''
        number = options.arabic

        # Find all the values and replace with letter
        for key in sorted(arabic.keys(), reverse=True):
            while number >= key:
                numerals += arabic[key][0]
                number -= key

        # Replace string of 4
        for index, key in enumerate(sorted(arabic.keys(), reverse=True)):
            if (arabic[key][0] * 4) in numerals:
                numerals = numerals.replace(arabic[key][0] * 4, arabic[key][1])
        logging.info(f'{options.arabic} -> {numerals}')


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


    parser = argparse.ArgumentParser(description=__description__,
                                     formatter_class=parser_formatter(argparse.RawTextHelpFormatter,
                                                                      indent_increment=4, max_help_position=12,
                                                                      width=160))

    numerals = parser.add_mutually_exclusive_group()
    numerals.add_argument('-rc', '--roman-case', default=None,
                          action='store', dest='roman_case',
                          metavar='CHARACTERS',
                          help='roman numerals MDCLXVImcdclxvi\n'
                               'i =     1        I =    1000\n'
                               'v =     5        V =    5000\n'
                               'x =    10        X =   10000\n'
                               'l =    50        L =   50000\n'
                               'c =   100        C =  100000\n'
                               'd =   500        D =  500000\n'
                               'm =  1000        M = 1000000\n')
    numerals.add_argument('-ru', '--roman-underscore', default=None,
                          action='store', dest='roman_score',
                          metavar='CHARACTERS',
                          help='roman numerals _M_D_C_L_X_V_IMCDLXVI\n'
                               'I =     1       _I =    1000\n'
                               'V =     5       _V =    5000\n'
                               'X =    10       _X =   10000\n'
                               'L =    50       _L =   50000\n'
                               'C =   100       _C =  100000\n'
                               'D =   500       _D =  500000\n'
                               'M =  1000       _M = 1000000\n')
    numerals.add_argument('-a', '--decimal', type=int, default=None,
                          action='store', dest='arabic',
                          help='arabic numerals 0-1000000')

    parser.add_argument('--debug', const=10, default=20,
                        action='store_const', dest='debug',
                        help=argparse.SUPPRESS)

    options = parser.parse_args()

    main()

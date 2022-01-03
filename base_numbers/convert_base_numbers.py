#!/usr/bin/env python3
"""
Script:	base_numbers.py
Date:	2022-01-01	

Platform: macOS/Windows/Linux

Description:

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2022, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'
__description__ = '''
    Convert between bases
'''

import argparse
import logging

SCALE = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    # Setup logging
    logging.basicConfig(format='{message}', level=options.debug, style='{')

    logging.debug(f'Options: {bases}')

    for base in bases.items():
        if base[1] == '?':
            convert_to = base[0]
        else:
            convert_from = base[0]
            number_from = base[1]

    logging.info(f'Converting number {number_from} (base-{convert_from}) to base-{convert_to}')

    # Convert to base-10
    if convert_from != 10:
        base10 = 0
        logging.debug('-' * 40)
        logging.debug('Converting to base-10')
        for index, digit in enumerate(number_from[::-1]):
            logging.debug(f'Digit:      {digit}')
            logging.debug(f'  Number:     {SCALE.find(digit)}')
            logging.debug(f'  Multiplier: {convert_from ** index}')
            base10 += (convert_from ** index) * SCALE.find(digit)
    else:
        base10 = int(number_from)
    logging.debug(f'Base-10: {base10}')

    # Convert from base-10
    if convert_to != 10:
        logging.debug('-' * 40)
        logging.debug(f'Converting to base-{convert_to}')

        number_to = f'{convert_base(base10, convert_to)[::-1]}'
    else:
        number_to = base10

    logging.debug('-' * 40)

    # Display conversion
    logging.info(f'{number_from} -> {number_to}')


def convert_base(decimal, base):
    """
    Convert base10 number into another base.
    :param decimal: (int) Base 10 number
    :param base: (int) Base to convert to
    :return: (str) New number
    """
    if decimal > (base - 1):
        remainder = convert_base(decimal // base, base)
        logging.debug(f'Decimal: {SCALE[decimal % base]} % {remainder}')
        return f'{SCALE[decimal % base]}{remainder}'
    else:
        return SCALE[decimal]


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


    # Create an argument parser
    parser = argparse.ArgumentParser(description=__description__,
                                     formatter_class=parser_formatter(argparse.RawTextHelpFormatter,
                                                                      indent_increment=4,
                                                                      max_help_position=12,
                                                                      width=160))

    # Placeholder for the arguments
    parser.add_argument('-<base>', '--<base>',
                        action='store', dest='number',
                        help='specify 2 bases (2-36). One with a number and one with a question mark\n'
                             'Examples:\n'
                             '\t-2 1010 -3 ? ...Convert base 2 number to base 3\n'
                             '\t-4=? -3 2222 ...Convert base 3 number to base 4\n'
                             '\t-5=123 --6=? ...Convert base 5 number to base 6\n')

    parser.add_argument('--debug', const=10, default=20,
                        action='store_const', dest='debug',
                        help=argparse.SUPPRESS)

    options, base_args = parser.parse_known_args()

    # Get all the arguments that cannot be specified traditionally
    bases = {}
    for index, arg in enumerate(base_args):
        if arg.startswith('-'):
            try:
                raw_arg = arg.lstrip('-')
                if '=' in arg:
                    key = raw_arg.split('=')[0]
                    value = raw_arg.split('=')[1].upper()
                else:
                    key = raw_arg
                    value = base_args[index + 1].upper()
            except IndexError:
                parser.error(f'argument {arg}: expected one argument')

            # Check that they have a key that is a number and in range
            try:
                bases[int(key)] = value
                if not 37 > int(key) > 1:
                    arg = arg.split('=')[0] if '=' in arg else arg
                    parser.error(f'unrecognized arguments: {arg}')
            except ValueError:
                arg = arg.split('=')[0] if '=' in arg else arg
                parser.error(f'unrecognized arguments: {arg}')

    # Check that we only got 2 arguments
    if len(bases.items()) != 2:
        parser.error(f'invalid amount of bases specified')

    # Check that one is a question mark
    if len([True for key in bases if bases[key] == '?']) != 1:
        parser.error(f'one argument must be a question mark "?"')

    # Check that the number can be valid for the base given
    for item in bases.items():
        if item[1] != '?':
            try:
                if any([True for digit in item[1] if SCALE.find(digit) >= item[0]]):
                    parser.error(f'{item[1]} is not a base {item[0]} number')
            except ValueError:
                parser.error(f'{item[1]} is not a base {item[0]} number')

    main()

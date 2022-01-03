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
    Convert binary to different bases
'''

import argparse
import logging


def main():
    # Setup logging
    logging.basicConfig(format='{message}', level=options.debug, style='{')

    result = 0
    for index, number in enumerate(options.binary[::-1]):
        result += (options.base ** index) * int(number)
        logging.debug(f'{index}: {options.base} ** {index} * {int(number)} ')
        logging.debug(f'\t= {options.base ** index} * {int(number)}')
        logging.debug(f'\t= {result}')

    logging.info(f'{options.binary} = {result}')


if __name__ == '__main__':

    def binary(binary_set):
        """
        Validate string is binary
        :param binary_set: (str) String of binary digits
        :return: argument, exception
        """
        if any([True for digit in binary_set if digit not in ('1', '0')]):
            parser.error(f'{binary_set} not a binary number')
        else:
            return binary_set


    parser = argparse.ArgumentParser(description=__description__)

    parser.add_argument(type=binary, default=None,
                        action='store', dest='binary',
                        help='binary representation on number')
    parser.add_argument(type=int, default=None,
                        action='store', dest='base',
                        help='base')

    parser.add_argument('--debug', const=10, default=20,
                        action='store_const', dest='debug',
                        help=argparse.SUPPRESS)

    options = parser.parse_args()

    main()

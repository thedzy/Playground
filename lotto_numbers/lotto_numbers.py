#!/usr/bin/env python3
"""
Script:	lotto_numbers.py
Date:	2021-12-30	

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
__description__ = '''
    lotto stats
'''

import argparse
import logging
import math


def main():
    # Setup logging
    logging.basicConfig(format='{message}', level=options.debug, style='{')

    logging.info('Some stats on the lottery, by someone who is not statistician\n')

    # https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310040901
    life_expectancy = 81.1

    odds = factorial(options.numbers, options.digits) / factorial(options.digits)
    logging.debug(f'({factorial(49, 6)} / {factorial(6)}) * ({factorial(43, 0)} / {factorial(0)})')

    lightning_odds = lightning(odds / 2)

    logging.info(f'Odds of winning the jackpot: 1 in {comma_format(odds)}')
    justification = len(str(odds))
    logging.info(f'{"Picks":^10} {"Odds":>{justification}}')
    logging.info(f'{"-" * 10} {"-" * justification}')
    for x in range(0, options.digits):
        digits = options.digits - x
        logging.debug(digits, options.numbers - x)
        logging.debug(f'({factorial(options.digits, digits)} / {factorial(digits)}) * '
                      f'({factorial(options.numbers - digits - x, x)} / {factorial(x)})')
        logging.debug(f'(factorial({options.digits}, {digits}) / factorial({digits})) * '
                      f'(factorial({options.numbers - digits - x}, {x}) / factorial({x}))')

        sub_odds = odds / ((
                                   factorial(options.digits, digits) / factorial(digits)
                           ) * (
                                   factorial(options.numbers - digits - x, x) / factorial(x)
                           ))
        logging.info(f'{digits:^10} {comma_format(int(sub_odds)):>{justification}}')
    logging.info(f'You will likely be struck by lightning between {lightning_odds} time(s) before winning the jackpot')

    print()

    for frequency, interval in (('day', 365,), ('week', 52,), ('month', 12,), ('year', 1,)):
        logging.info(f'PLAY EVERY {frequency.upper()}')
        logging.info(f'Years to likely win if you played every '
                     f'{frequency} {comma_format(odds / interval / 2)}')
        logging.info(f'Lifetimes to likely win if played every '
                     f'{frequency} {comma_format(odds / interval / life_expectancy / 2)}')
        logging.info(f'Years to guarantee a win if you played every '
                     f'{frequency} {comma_format(odds / interval)}')
        logging.info(f'Lifetimes to guarantee a win if played every '
                     f'{frequency} {comma_format(odds / interval / life_expectancy)}')
        logging.info(f'You will have to play {comma_format(int(odds / (interval * (life_expectancy - 18))) + 1)} '
                     f'times a {frequency} to guarantee a win in your lifetime')
        logging.info(f'Playing once a {frequency} at ${options.price} a ticket you will only save '
                     f'${comma_format(int(interval * (life_expectancy - 18) * options.price))} '
                     f'by not playing')

        print()

    logging.info(f'Cost of likely win the jackpot ${comma_format(options.price * odds / 2)}')
    logging.info(f'Cost to guarantee the jackpot ${comma_format(options.price * odds)}')


    print()


def factorial(number, digits=None):
    """
    Calculate factorial to x digits
    :param number: (int) Number
    :param digits: (int) Quantity of numbers
    :return: (int) Possibilities
    """
    digits = number if digits is None else digits
    # Cannot have more digits than numbers
    if digits > number:
        logging.error('You cannot have more selections that available numbers')
        exit()

    if number == 0 or digits == 0:
        return 1
    else:
        if digits > 1:
            return (number - digits + 1) * factorial(number, digits - 1)
        else:
            return number


def lightning(number):
    # Odds of lighting striking
    # https://www.canada.ca/en/environment-climate-change/services/lightning/safety/fatalities-injury-statistics.html
    # https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901
    lighning_odds = 213758

    for chance in range(1, 100):
        if lighning_odds > number:
            break
        else:
            lighning_odds = lighning_odds * lighning_odds

    return f'{chance - 1} and {chance}'


def comma_format(number, decimals=1):
    if isinstance(number, float):
        str_number = f'{number:0.{decimals}f}'
    else:
        str_number = str(number)
    if '.' in str_number:
        str_number, decimals = str_number.split('.')
    else:
        decimals = ''

    new_number = []
    for index, character in enumerate(str_number[::-1]):
        if index % 3 == 0 and index != 0:
            new_number.append(',')
        new_number.append(character)

    if isinstance(number, float):
        return ''.join(new_number[::-1]) + '.' + decimals
    else:
        return ''.join(new_number[::-1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__description__)

    parser.add_argument('-d', '--digits', type=int,
                        action='store', dest='digits',
                        required=True,
                        help='how many numbers do you have to pick?')

    parser.add_argument('-n', '--number', type=int,
                        action='store', dest='numbers',
                        required=True,
                        help='how large are the numbers')

    parser.add_argument('-p', '--price', type=int, default=1,
                        action='store', dest='price',
                        help='price of a ticket')

    parser.add_argument('--debug', const=10, default=20,
                        action='store_const', dest='debug',
                        help=argparse.SUPPRESS)

    options = parser.parse_args()

    main()

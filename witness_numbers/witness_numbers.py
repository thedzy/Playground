#!/usr/bin/env python3
"""
Script:	witness_numbers.py
Date:	2021-12-26	

Platform: macOS/Windows/Linux
"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2021, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'
__description__ = '''
    Test witness numbers for prime
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    https://www.youtube.com/watch?v=_MscGSN5J6o&ab_channel=Numberphile
'''

import argparse
import random
import logging


def main():
    """
    While I don't like 1 letter variables as they don't clarify what the data is,
    I have used them to stay inline with the formulas
    :return: (void)
    """

    # Setup logging to screen
    logging.basicConfig(filename=None, format='{message}', level=options.debug, style='{')

    # Get number
    n = options.number
    logging.debug(f'Number is {n}')

    # Filter out anything that will not calculate
    if n == 1:
        logging.debug('Come on. 1 is not prime')
        logging.info(f'{n} is not Prime')
        exit()
    if n % 2 == 0:
        logging.debug('Come on. don\'t be crazy, that\'s an even number')
        logging.info(f'{n} is not Prime')
        exit()

    # Get a list of witnesses
    if n < 2047:
        logging.debug('Less than 2047')
        unused_witnesses = [2]
        probability = 1
    elif n < 1373653:
        logging.debug('Less than 1373653')
        unused_witnesses = [2, 3]
        probability = 1
    elif n < 9080191:
        logging.debug('Less than 9080191')
        unused_witnesses = [31, 73]
        probability = 1
    elif n < 25326001:
        logging.debug('Less than 25326001')
        unused_witnesses = [2, 3, 5]
        probability = 1
    elif n < 3215031751:
        logging.debug('Less than 3215031751')
        unused_witnesses = [2, 3, 5, 7]
        probability = 1
    elif n < 4759123141:
        logging.debug('Less than 4759123141')
        unused_witnesses = [2, 7, 61]
        probability = 1
    elif n < 1122004669633:
        logging.debug('Less than 1122004669633')
        unused_witnesses = [2, 13, 23, 1662803]
        probability = 1
    elif n < 2152302898747:
        logging.debug('Less than 2152302898747')
        unused_witnesses = [2, 3, 5, 7, 11]
        probability = 1
    elif n < 3474749660383:
        logging.debug('Less than 3474749660383')
        unused_witnesses = [2, 3, 5, 7, 11, 13]
        probability = 1
    elif n < 341550071728321:
        logging.debug('Less than 341550071728321')
        unused_witnesses = [2, 3, 5, 7, 11, 13, 17]
        probability = 1
    else:
        logging.debug('More than  or equal to 341550071728321')
        unused_witnesses = list(range(1, n))
        # 25% is sufficient when testing from a full set
        probability = 0.25

    # Loop through witnesses
    while True:
        # Divider
        logging.debug('_' * 40)
        logging.debug(f'Test {(n - len(unused_witnesses))} of {n * probability}')
        logging.debug('_' * 40)

        # Pick a witness
        a = random.choice(unused_witnesses)
        logging.debug(f'a: {a}')
        unused_witnesses.remove(a)

        # Check if we reached required probability
        if (n - len(unused_witnesses)) >= (n * probability) + 1:
            logging.info(f'{n} is Prime')
            break

        # Get highest power of 2
        m = highest_power(n)
        logging.debug(f'm: {m}')

        # Get exponent
        d = n // (2 ** m)
        logging.debug(f'd: {d}')

        # Get answer
        answer = a ** d % n
        logging.debug(f'2 ^ {m} * {d} + 1 = {n}')
        logging.debug(((2 ** m) * d) + 1)

        # Print formula
        logging.debug(f'a ^ d % n = answer')
        logging.debug(f'{a} ^ {d} % {n} = {answer}')

        # Print likelihood
        if answer == 1 or (answer - n) == -1:
            logging.debug(f'{a} says {n} is Prime')
        else:
            logging.debug(f'{a} says {n} is not Prime')
            if options.display_primes:
                logging.info(f'{n} is not Prime')
            break

        if len(unused_witnesses) == 0:
            logging.info(f'{n} is Prime')
            break


def highest_power(number):
    """
    Get highest power of 2 that evenly divides
    :param number: (int) Number to test against
    :return: (int) Power
    """
    new_power = 1
    while 2 ** new_power < (number + 1):
        if number % new_power == 0:
            power = new_power
        new_power = new_power * 2
    return power


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__description__)

    # Positional argument
    parser.add_argument(type=int,
                        dest='number',
                        help='number to test')

    # Display primes only, useful for searching ranges
    parser.add_argument('-p', '--only-primes', default=True,
                        action='store_false', dest='display_primes',
                        help='display results only if prime')

    # Debug
    parser.add_argument('--debug', const=10, default=20,
                        action='store_const', dest='debug',
                        help=argparse.SUPPRESS)

    options = parser.parse_args()

    main()

#!/usr/bin/env python3
"""
Script:	van_eck_sequence.py
Date:	2020-05-20	

Platform: macOS/Windows/Linux

Description:
Generates the van eck sequence of numbers
"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2020, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'


def main():
    length = 1000
    max_value = 1000

    # Get sequence of fixed length
    sequence = get_sequence(length)
    print(sequence)
    print('Length', len(sequence))

    # Get sequence until a value (or above is reached)
    sequence = get_sequence(max_value=max_value)
    print(sequence)
    print('Length', len(sequence))

def get_sequence(length=None, max_value=0):
    sequence = [0]
    counter = 1
    while True:
        counter += 1
        digit_compare = sequence[-1]
        sequence_previous = sequence[:-1]

        if length is None:
            if max_value <= digit_compare:
                break
        else:
            if counter > length:
                break

        if digit_compare not in sequence_previous:
            sequence.append(0)
        else:
            sequence.append(sequence_previous[::-1].index(digit_compare) + 1)



    return sequence


if __name__ == '__main__':
    main()

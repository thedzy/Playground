#!/usr/bin/env python3
"""
Script:	binary_reversal_coderbytes.py.py
Date:	2020-05-17	

Platform: macOS/Windows/Linux

Description:
Binary Reversal
Have the function BinaryReversal(str) take the str parameter being passed, which will be a positive integer, take its
binary representation (padded to the nearest N * 8 bits), reverse that string of bits, and then finally return the new
reversed string in decimal form. For example: if str is "47" then the binary version of this integer is 101111 but we
pad it to be 00101111. Your program should reverse this binary string which then becomes: 11110100 and then finally
return the decimal version of this string, which is 244.
Examples

Input: "213"
Output: 171

Input: "4567"
Output: 60296

Tags
string manipulation, free

URL: https://coderbyte.com/editor/Binary%20Reversal:Python3
"""
__author__ = "thedzy"
__copyright__ = "Copyright 2020, thedzy"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "thedzy"
__email__ = "thedzy@hotmail.com"
__status__ = "Developer"


def main():
    print('Result:', BinaryReversal(input('Integer: ')))


def BinaryReversal(str):
    """
    See description
    :param str: (str) String representation of integer
    :return: (int) Int representation of a binary reversed
    """
    # Convert to binary string
    binary = bin(int(str)).lstrip('0b')
    # Find how many multiples of 8 lengths we need
    padding, remainder = divmod(len(binary), 8)
    padding = padding if remainder == 0 else padding + 1
    # Pad the string
    binary = binary.rjust(8 * padding, '0')[::-1]

    # Convert and return
    return int(binary, base=2)


if __name__ == '__main__':
    main()

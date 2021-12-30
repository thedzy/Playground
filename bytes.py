#!/usr/bin/env python3
"""
Script:	bytes.py
Date:	2021-12-30

Platform: macOS/Windows/Linux

Description:
    Fun with bytes
"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2021, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'


def main():
    width = 50
    print(f'{" " * (width - 1)}Bytes')
    sizes = {
        0: 'B', 10: 'KB', 20: 'MB', 30: 'GB', 40: 'TB', 50: 'PB', 60: 'EB', 70: 'ZB', 80: 'YB', 90: 'BB', 100: '?B'
    }
    for index, size in enumerate(sizes):
        number = 1 << size
        print(f'{comma_format(number)} {sizes[size]:>2}'.rjust(width), f' = 1024^{index}')


def comma_format(number):
    str_number = list(str(number))
    len_number = len(str_number)

    for index in range(0, int(len_number / 3)):
        str_number.insert((index * 3) + index + 1, ',')

    return ''.join(str_number)


if __name__ == '__main__':
    main()

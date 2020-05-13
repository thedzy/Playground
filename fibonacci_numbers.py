#!/usr/bin/env python3
"""
Script:	fibonacci_numbers.py
Date:	2020-05-13	

Platform: macOS/Windows/Linux

Description:
Somehow thought this would be harder, so here is a sequence generator for fibonacci numbers
"""
__author__ = "thedzy"
__copyright__ = "Copyright 2020, thedzy"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "thedzy"
__email__ = "thedzy@hotmail.com"
__status__ = "Developer"


def main():
    for n in range(1000):
        print('fibonacci({:2}) : {}'.format(n, fibonacci(n)))


def fibonacci(n):
    n1, n2 = 1, 0
    index = 0
    sum_of_values = 0
    while True:
        if n <= index:
            return sum_of_values

        sum_of_values = n1 + n2
        n1, n2 = n2, sum_of_values

        index += 1


if __name__ == '__main__':
    main()

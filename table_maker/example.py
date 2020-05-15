#!/usr/bin/env python3
"""
Script:	example.py
Date:	2020-02-22

Platform: macOS/Windows/Linux

Description:
Create a pretty print table example
"""
__author__ = "thedzy"
__copyright__ = "Copyright 2020, thedzy"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "thedzy"
__email__ = "thedzy@hotmail.com"
__status__ = "Developer"

import random

import table_maker


def main():
    with open('/usr/share/dict/propernames', 'r') as names_file:
        first_names = names_file.read().split('\n')

    with open('/usr/share/dict/words', 'r') as names_file:
        last_names = names_file.read().split('\n')

    with table_maker.Table(padding=3, align='left', header_align='left', min=10, title='Money owing') as table:
        name_count = random.randint(2, 9)
        totals = [0] * name_count

        cols = []
        for col in range(name_count):
            cols.append('{}\n{}'.format(random.choice(first_names), random.choice(last_names).title()))
        table.set_header(*cols)

        for row in range(random.randint(1, 20)):
            row = []
            for index in range(random.randint(1, name_count)):
                amount = random.randrange(1, 999999) / 100
                row.append('{:,.2f}'.format(amount))
                totals[index] += amount
            table.append_row(*row)

        cols = []
        for total in totals:
            cols.append('{:,.2f}'.format(total))
        table.set_footer(*cols)

        table.set_title('Money Owed')
        table.padding(1)
        table.min(25)
        table.even(True)
        table.align('right')
        table.header_align('centre')
        table.footer_align('right')

    with table_maker.Table(padding=1, align='centre', min=3) as table:
        table.set_title('Multiplication')

        table.set_rows([[00, 1, 2, 3, 4, 5],
                        [1, 1, 2, 3, 4, 5],
                        [2, 2, 4, 6, 8, 10],
                        [3, 3, 6, 9, 12, 15],
                        [4, 4, 8, 12, 15, 20]])
        table.append_row(5, 5, 10, 15, 20, 25)
        pass


if __name__ == '__main__':
    main()

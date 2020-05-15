#!/usr/bin/env python3
"""
Script:	table_maker.py
Date:	2020-02-22

Platform: macOS/Windows/Linux

Description:
Create a pretty print table
"""
__author__ = "thedzy"
__copyright__ = "Copyright 2020, thedzy"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "thedzy"
__email__ = "thedzy@hotmail.com"
__status__ = "Developer"


class Table:
    def __init__(self, **kwargs):
        self.__headers = []
        self.__footers = []
        self.__rows = []
        self.__col_widths = []

        self.__title = kwargs['title'] if 'title' in kwargs else None

        self.__padding = kwargs['padding'] if 'padding' in kwargs else 0

        self.__min_width = kwargs['min'] if 'min' in kwargs else 3
        self.__even_width = bool(kwargs['even']) if 'even' in kwargs else False

        self.__alignments = {
            'l': '<',
            'r': '>',
            'c': '^'
        }

        if 'align' in kwargs:
            self.__data_align = self.__alignments.get(kwargs['align'][0], '^')
            self.__header_align = self.__alignments.get(kwargs['align'][0], '^')
            self.__footer_align = self.__alignments.get(kwargs['align'][0], '^')

        if 'data_align' in kwargs:
            self.__data_align = self.__alignments.get(kwargs['data_align'][0], '^')

        if 'header_align' in kwargs:
            self.__header_align = self.__alignments.get(kwargs['header_align'][0], '^')

        if 'footer_align' in kwargs:
            self.__footer_align = self.__alignments.get(kwargs['footer_align'][0], '^')

    def __del__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.print()

    def padding(self, padding=None):
        if padding is not None:
            self.__padding = int(padding)

        return self.__padding

    def min(self, min_width=None):
        if min_width is not None:
            self.__min_width = int(min_width)

        return self.__min_width

    def even(self, even_width=None):
        if even_width is not None:
            self.__even_width = bool(even_width)

        return self.__even_width

    def align(self, align=None):
        if align is not None:
            self.__data_align = self.__alignments.get(align[0], '^')
            self.__header_align = self.__alignments.get(align[0], '^')
            self.__footer_align = self.__alignments.get(align[0], '^')

        return self.__data_align

    def data_align(self, align=None):
        if align is not None:
            self.__data_align = self.__alignments.get(align[0], '^')

        return self.__data_align

    def header_align(self, align=None):
        if align is not None:
            self.__header_align = self.__alignments.get(align[0], '^')

        return self.__header_align

    def footer_align(self, align=None):
        if align is not None:
            self.__footer_align = self.__alignments.get(align[0], '^')

        return self.__footer_align

    def get_title(self):
        return self.__title

    def set_title(self, title=None):
        self.__title = title

    def set_header(self, *args):
        cols = len(args)
        rows = 0
        header_titles = list(args)

        # Get size of the matrix
        for arg_index in range(len(header_titles)):
            header_titles[arg_index] = header_titles[arg_index].split('\n')
            if len(header_titles[arg_index]) > rows:
                rows = len(header_titles[arg_index])

        # Flip matrix
        self.__headers = []
        for row in range(rows):
            row_list = []
            for col in range(cols):
                try:
                    row_list.append(header_titles[col][row])
                except:
                    row_list.append('')
            self.__headers.append(row_list)

    def set_footer(self, *args):
        cols = len(args)
        rows = 0
        footer_titles = list(args)

        # Get size of the matrix
        for arg_index in range(len(footer_titles)):
            footer_titles[arg_index] = str(footer_titles[arg_index]).split('\n')
            if len(footer_titles[arg_index]) > rows:
                rows = len(footer_titles[arg_index])

        # Flip matrix
        self.__footers = []
        for row in range(rows):
            row_list = []
            for col in range(cols):
                try:
                    row_list.append(footer_titles[col][row])
                except:
                    row_list.append('')
            self.__footers.append(row_list)

    def set_rows(self, matrix=None):
        if matrix is None:
            matrix = [[]]
        self.__rows = matrix

    def append_row(self, *args):
        self.__rows.append(list(args))

        arg_counts = len(args)
        col_counts = len(self.__col_widths)
        if col_counts < arg_counts:
            self.__col_widths.extend([0] * (arg_counts - col_counts))

    def print(self):
        self.__calculate_colums()

        cols_count = len(self.__col_widths)

        if self.__even_width:
            max_width = max(*self.__col_widths, self.__min_width)
            self.__col_widths = [max_width] * len(self.__col_widths)

        alignment = [self.__data_align, self.__header_align, self.__footer_align]
        strings = [''] * 3
        for index in range(0, 3):
            for col_index in range(cols_count):
                strings[index] += '|{1}{{{2}:{0}{3}}}{1}'.format(alignment[index], ' ' * self.__padding, col_index,
                                                                 self.__col_widths[col_index])
            strings[index] += '|'

        row_format, head_format, foot_format = strings

        if self.__title is not None:
            self.__divider()
            title_format = '|{0}{1}{2}|'
            # Title title space
            space = (sum(self.__col_widths) + cols_count + (self.__padding * cols_count * 2))
            for line in self.__title.split('\n'):
                # Trim title to the space available
                title = line[:(space - 1)]
                # Get left and right space to centre title
                left = int((space - len(line)) / 2)
                right = int(space - len(line)) - left - 1
                # Print
                print(title_format.format(' ' * left, title, ' ' * right))

        # Print table
        self.__divider()

        if len(self.__headers) > 0:
            for header in self.__headers:
                header.extend([''] * (cols_count - len(header)))
                print(head_format.format(*header))
            self.__divider('=', '|')

        if len(self.__rows) > 0:
            for row in self.__rows:
                row.extend([''] * (cols_count - len(row)))
                print(row_format.format(*row))
            self.__divider('-', '|')

        if len(self.__footers) > 0:
            for footer in self.__footers:
                footer.extend([''] * (cols_count - len(footer)))
                print(foot_format.format(*footer))
            self.__divider()

    def __divider(self, symbol='-', intersection='+'):
        cols_count = len(self.__col_widths)

        # Build a diver string
        divider = ''
        for col_index in range(cols_count):
            divider += '{}{}'.format(intersection[0], symbol[0] * (self.__col_widths[col_index] + (self.__padding * 2)))
        divider += intersection[0]

        print(divider)

    def __calculate_colums(self):
        # Parse through and find the required column widths
        for section in [self.__headers, self.__rows, self.__footers]:
            if len(section) > 0:
                for row in section:
                    col_counts = len(self.__col_widths)
                    row_counts = len(row)
                    if col_counts < row_counts:
                        self.__col_widths.extend([0] * (row_counts - col_counts))

                for col_index in range(len(row)):
                    if len(str(row[col_index])) > self.__col_widths[col_index] or self.__min_width > self.__col_widths[
                        col_index]:
                        self.__col_widths[col_index] = max(len(str(row[col_index])), self.__min_width)

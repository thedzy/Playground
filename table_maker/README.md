# table_maker.py

Pretty print a table of data
```
+---------------------------+---------------------------+---------------------------+---------------------------+---------------------------+---------------------------+
|                                                                               Money Owed                                                                              |
+---------------------------+---------------------------+---------------------------+---------------------------+---------------------------+---------------------------+
|          Rodney           |         Wolfgang          |           Vijay           |           Lewis           |            Jun            |         Charlene          |
|           Enoil           |          Expire           |           Amort           |       Galactometer        |       Quadrumanous        |         Twaesome          |
|===========================|===========================|===========================|===========================|===========================|===========================|
|                  7,796.21 |                           |                           |                           |                           |                           |
|                  6,693.75 |                  4,796.02 |                  4,709.13 |                           |                           |                           |
|                  2,858.45 |                     94.93 |                           |                           |                           |                           |
|                  5,357.84 |                           |                           |                           |                           |                           |
|                  4,098.49 |                  2,033.44 |                  2,610.73 |                  1,862.91 |                           |                           |
|                    813.40 |                  9,005.59 |                           |                           |                           |                           |
|                  1,930.03 |                           |                           |                           |                           |                           |
|                  5,788.21 |                  4,331.52 |                  1,684.86 |                           |                           |                           |
|                  3,641.04 |                  2,846.55 |                  5,970.60 |                  1,745.96 |                    226.51 |                           |
|                    306.70 |                  4,138.23 |                  3,468.88 |                           |                           |                           |
|                  9,824.43 |                  4,707.84 |                  9,824.70 |                  9,729.86 |                  8,812.01 |                           |
|                  7,003.83 |                  5,899.56 |                  6,600.01 |                           |                           |                           |
|                  5,733.39 |                    413.84 |                           |                           |                           |                           |
|                  7,764.71 |                  6,348.55 |                  3,969.27 |                  1,312.46 |                           |                           |
|                  8,656.73 |                  2,657.19 |                  8,769.27 |                           |                           |                           |
|                  6,374.99 |                           |                           |                           |                           |                           |
|                    122.35 |                  5,259.30 |                    290.90 |                     30.66 |                  1,720.78 |                  9,920.62 |
|                  8,155.11 |                  6,636.35 |                  3,203.50 |                  4,646.80 |                  1,055.15 |                           |
|                  2,277.20 |                  5,586.70 |                  5,477.82 |                  7,317.23 |                           |                           |
|                  9,402.22 |                  1,835.27 |                  3,881.62 |                  2,790.76 |                  5,129.05 |                           |
|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
|                104,599.08 |                 66,590.88 |                 60,461.29 |                 29,436.64 |                 16,943.50 |                  9,920.62 |
+---------------------------+---------------------------+---------------------------+---------------------------+---------------------------+---------------------------+``

## What?

Takes a piece of data or continually add data to it and print it.  Supports title, headers, footers and alignment
```bash
class Table:
    def __init__(self, **kwargs):

    def __del__(self):

    def __enter__(self):

    def __exit__(self, exc_type, exc_val, exc_tb):

    def padding(self, padding=None):

    def min(self, min_width=None):

    def even(self, even_width=None):

    def align(self, align=None):

    def data_align(self, align=None):

    def header_align(self, align=None):

    def footer_align(self, align=None):

    def get_title(self):

    def set_title(self, title=None):

    def set_header(self, *args):

    def set_footer(self, *args):

    def set_rows(self, matrix=None):

    def append_row(self, *args):

    def print(self):

    def __divider(self, symbol='-', intersection='+'):

    def __calculate_colums(self):

```

## Why?
Just to see that I could.  Could have some useful code for other scripts or maybe cleaned up and refined into something useful. I believe this is built into numpy (not sure).

## Improvements?
Everything.  Alignments per cell, using ascii border characters, etc

## State?
No known bugs.  Not well tested, but something quickly hashed out and unrefined \
Virtually no comments.

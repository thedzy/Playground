# base_numbers.py
## Convert binary to different bases

Playing around with binary numbers.

### usage:
```
usage: base_numbers.py [-h] binary base

Convert binary to different bases

positional arguments:
  binary      binary representation on number
  base        base

optional arguments:
  -h, --help  show this help message and exit
```

# convert_base_numbers.py
## Convert between bases

Converts any base to another base from 2-36

Just playing with bases.  
The argument parser is useful for parsing undefined arguments.  
In this example, arguments 2-36 are not defined but work and are validated.  

### usage:
```
usage: convert_base_numbers.py [-h] [-<base> NUMBER]

    Convert between bases

optional arguments:
    -h, --help
            show this help message and exit
    -<base> NUMBER, --<base> NUMBER
            specify 2 bases (2-36). One with a number and one with a question mark
            Examples:
            	-2 1010 -3 ? ...Convert base 2 number to base 3
            	-4=? -3 2222 ...Convert base 3 number to base 4
            	-5=123 --6=? ...Convert base 5 number to base 6
```


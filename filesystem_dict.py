#!/usr/bin/env python3
"""
Script:	filesystem_dict.py
Date:	2020-05-31	

Platform: macOS/Windows/Linux

Description:
Turn the directory structure into a dict representation including sizes for each including its children

Created this for another project, but this component can stand on it's own.
"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2020, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'

import json
from pathlib import PurePath, Path


def main():
    base = Path('~/Downloads/').expanduser()
    print('Starting at: ', base)

    # For testing remove the .DS_Stores, why Apple? Why?
    for file in Path(base).rglob('.DS_Store'):
        if file.is_file():
            print('Removed:', file)
            file.unlink()

    dir_dict = get_dir_as_dict(base)

    print(json.dumps(dir_dict, indent=8))
    # Use 1000 if your computer uses base10 for size calculations
    print('Directory size: {:0.3f} {}'.format(dir_dict['size'] / 1024 / 1024, 'MB'))


def get_dir_as_dict(base):
    # Initialise
    dir_dict = {}

    # Traverse to build out the structure
    directories = list(Path(base).rglob('**'))
    for directory in directories:
        relative_path = Path(directory).relative_to(Path(base))
        sub_dict = dir_dict
        for item in PurePath(relative_path).parts:
            if item not in sub_dict:
                sub_dict[item] = {}
            sub_dict = sub_dict[item]

    # Reverse traverse to fill in the sizes
    for directory in reversed(directories):
        relative_path = Path(directory).relative_to(Path(base))
        sub_dict = dir_dict
        for item in PurePath(relative_path).parts:
            sub_dict = sub_dict[item]

        # Get the sum of all the files
        sum_of_files = 0
        file_count = 0
        for child in Path(directory).iterdir():
            child_path = Path(directory, child)
            if child_path.is_file():
                file_count += 1
                sum_of_files += child_path.stat().st_size

        # Get the sum of all the child directories, using values from the child dicts
        sum_of_dirs = 0
        for key in sub_dict:
            sum_of_dirs += sub_dict[key]['size']

        # Append the sum of the files and directory
        sub_dict['size'] = sum_of_files + sum_of_dirs
        sub_dict['file_count'] = file_count

    return dir_dict


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-09-22
Purpose: Python cat
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+')

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true',
                        default='False')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for file in args.file:
            if os.path.isfile(file):
                output=open(file).read()
                if args.number == True:
                    print(output)
                else:
                    print(output)


# --------------------------------------------------
if __name__ == '__main__':
    main()

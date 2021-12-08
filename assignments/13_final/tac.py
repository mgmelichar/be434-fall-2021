#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-12-07
Purpose: BE 534 Final
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='BE 534 Final: tac.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        nargs='+')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main function"""

    args = get_args()

    for f in args.file:
        if args.file:
            lines = f.readlines()
            for line in reversed(lines):
                print(line, end='', file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()

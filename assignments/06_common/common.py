#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-10-11
Purpose: common.py
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='common.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('FILE2',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='input file 2')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    set_1 = set(args.FILE1.read().rstrip().split())
    set_2 = set(args.FILE2.read().rstrip().split())
    common = list(set_1.intersection(set_2))
    common.sort()
    print(*common, sep="\n", file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()

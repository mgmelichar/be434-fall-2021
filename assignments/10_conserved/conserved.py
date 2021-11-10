#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-11-08
Purpose: Multiple Sequence Alignment
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='conserved.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    FILE = args.FILE.read().strip()
    seqs = FILE.splitlines()

    print(FILE)

    for i in range(len(seqs[0])):
        bases = [base[i] for base in seqs]
        if bases.count(bases[0]) == len(bases):
            print("|", end='')
        else:
            print("X", end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()

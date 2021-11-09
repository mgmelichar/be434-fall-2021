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
    seqs = FILE.split("\n")
    final_line = []

    for i in range(len(seqs[0])):
        pairs = [base[i] for base in seqs]
        if pairs.count(pairs[0]) == len(pairs):
            final_line.append("|")
        else:
            final_line.append("X")

    print(FILE)
    print(''.join(final_line))


# --------------------------------------------------
if __name__ == '__main__':
    main()

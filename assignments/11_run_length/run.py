#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-11-16
Purpose: Run-Length Encoding of DNA
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-Length Encoding of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna',
                        type=str,
                        help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------
def rle(dna):
    """Run length encoding
    https://stackabuse.com/run-length-encoding/ """

    encoding = ''
    prev_base = ''
    k = 1

    for base in dna:
        # If not previous base
        if base != prev_base:
            # Add count and base prior to encoding (finish)
            if prev_base:
                if k != 1:
                    encoding += prev_base + str(k)
                else:
                    encoding += prev_base
            k = 1
            prev_base = base
        else:
            # If previous base add to count
            k += 1

    # Final base encoding
    if dna:
        if k != 1:
            encoding += prev_base + str(k)
        else:
            encoding += prev_base

    return encoding


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if "/" in args.dna:
        dna_seq = open(args.dna, "rt").read().rstrip().splitlines()
        for base in dna_seq:
            print(rle(base))
    else:
        print(rle(args.dna))


# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-10-13
Purpose: iupac.py
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='str',
                        help='Input sequence(s)',
                        nargs='+')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    IUPAC = dict(A="A", C="C", G="G", T="T", U="U", R="AG", Y="CT", S="GC",
                 W="AT", K="GT", M="AC", B="CGT", D="AGT", H="ACT", V="ACG",
                 N="ACGT")
    for dna in args.seq:
        reg = ["["+IUPAC[val]+"]" if len(IUPAC[val])
               > 1 else IUPAC[val] for val in dna]
        print(dna, "".join(reg), file=args.outfile)
    if args.outfile != sys.stdout:
        print('Done, see output in "{}"'.format(args.outfile.name))


# --------------------------------------------------
if __name__ == '__main__':
    main()

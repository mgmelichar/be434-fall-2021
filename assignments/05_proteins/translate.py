#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-10-05
Purpose: translate.py
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='translate.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='str',
                        type=str,
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        required=True)

    parser.add_argument('-o',
                        '--output',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    key = args.codons.read().strip()
    base_list = [args.seq[i:i+3].upper() for i in range(0, len(args.seq), 3)]
    base_val = [key.find(base) for base in base_list]

    print(''.join(["-" if val == -1 else key[val+4]
          for val in base_val]), file=args.output)
    print('Output written to "{}".'.format(args.output.name))


# --------------------------------------------------
if __name__ == '__main__':
    main()

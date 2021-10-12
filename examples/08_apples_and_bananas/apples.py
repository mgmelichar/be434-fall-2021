#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-10-11
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    args= parser.parse_args()

    if os.path.isfile(args.text):
        args.text=open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)



# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-09-13
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',                                  # '+' means one or more
                        help='A positional argument')

    parser.add_argument('sort',
                    help='Sort list',
                    action='store_true')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if len(args.items) == 1:
        print('You are bringing '+args.items[0]+'.')
    elif len(args.items) == 2:
        print('You are bringing '+' and '.join(args.items)+'.')
    else:
        print('You are bringing {}, and {}.'.format(", ".join(args.items[:-1]),args.items[-1]))


# --------------------------------------------------
if __name__ == '__main__':
    main()

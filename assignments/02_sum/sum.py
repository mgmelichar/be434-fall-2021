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

    parser.add_argument('int',
                        help='Numbers to add',
                        metavar='int',
                        nargs='+', 
                        type=int)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    string_int=[]

    for int in args.int:
        string_int.append(str(int))

    print(' + '.join(string_int) + ' = ' + str(sum(args.int)))


# --------------------------------------------------
if __name__ == '__main__':
    main()

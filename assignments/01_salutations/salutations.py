#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-09-01
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        metavar='str',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet',
                        metavar='str',
                        type=str,
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    greeting_arg = args.greeting
    name_arg = args.name

    if args.excited:
        flag_arg='!'
    else:
        flag_arg='.'

    print(greeting_arg+', '+name_arg+flag_arg)


# --------------------------------------------------
if __name__ == '__main__':
    main()

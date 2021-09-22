#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-09-19
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('solfege',
                        metavar='str',
                        nargs='+',
                        help='solfege')

    return parser.parse_args()

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    solfege_list = dict(
        Do='A deer, a female deer',
        Re='A drop of golden sun',
        Mi='A name I call myself',
        Fa='A long long way to run',
        Sol='A needle pulling thread',
        La='A note to follow sol',
        Ti='A drink with jam and bread')

    for syl in args.solfege:
        if syl in solfege_list:
            print('{}, {}'.format(syl, solfege_list[syl]))
        else:
            print('I don\'t know "{}"'.format(syl))


# --------------------------------------------------
if __name__ == '__main__':
    main()

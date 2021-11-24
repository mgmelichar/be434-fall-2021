#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-11-23
Purpose: grep.py
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='greop.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='str',
                        help='Search pattern')

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    out = []
    args = get_args()
    for text in args.FILE:
        for line in text:

            # Optional ending
            if '?' in args.pattern:
                pattern_2 = args.pattern[0:-2]

                if args.insensitive is True:
                    # Optional ending, insensitive search
                    if line.find(pattern_2) != -1:
                        out.append(line)
                    if line.find(pattern_2.capitalize()) != -1:
                        out.append(line)
                    if line.find(pattern_2.upper()) != -1:
                        out.append(line)
                    if line.find(pattern_2.lower()) != -1:
                        out.append(line)
                else:
                    # Optional ending, sensitive search
                    if line.find(pattern_2) != -1:
                        out.append(line)
            else:
                # insensitive search
                if args.insensitive is True:
                    # NO optional ending, insensitive
                    if line.find(args.pattern.capitalize()) != -1:
                        out.append(line)
                    if line.find(args.pattern.upper()) != -1:
                        out.append(line)
                    if line.find(args.pattern.lower()) != -1:
                        out.append(line)
                else:
                    # NO optional ending, sensitive search
                    if line.find(args.pattern) != -1:
                        out.append(line)
    for i in out:
        print(i.strip(), file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()

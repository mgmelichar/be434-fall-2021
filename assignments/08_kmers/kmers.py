#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-10-25
Purpose: kmers.py
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('FILE2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='input file 2')

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    f1 = args.FILE1.read().rstrip().split()
    f2 = args.FILE2.read().rstrip().split()

    k1 = []
    k2 = []

    counts1 = {}
    counts2 = {}

    for word in f1:
        n = len(word) - args.kmer + 1
        if n >= 1:
            for i in range(n):
                seq = word[i:i + args.kmer]
                k1.append(seq)

                if seq in counts1:
                    counts1[seq] += 1
                else:
                    counts1[seq] = 1

    for word in f2:
        n = len(word) - args.kmer + 1
        if n >= 1:
            for i in range(n):
                seq = word[i:i + args.kmer]
                k2.append(seq)

                if seq in counts2:
                    counts2[seq] += 1
                else:
                    counts2[seq] = 1

    set_1 = set(k1)
    set_2 = set(k2)
    common = list(set_1.intersection(set_2))

    for word in common:
        print('{0:<10} {1:>5} {2:>5}'.format(
            word, counts1[word], counts2[word]))


# --------------------------------------------------
if __name__ == '__main__':
    main()

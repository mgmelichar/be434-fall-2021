#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-11-01
Purpose: Assignemnt 09_fasta
"""

import argparse
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='au_pair.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs="+",
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        default="split")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    for file in args.FILE:
        root, ext = os.path.splitext(os.path.basename(file.name))
        forward = open(os.path.join(args.outdir, root + "_2" + ext), "wt")
        reverse = open(os.path.join(args.outdir, root + "_1" + ext), "wt")

        for i, record in enumerate(SeqIO.parse(file, "fasta")):
            SeqIO.write(record, forward if i % 2 == 0 else reverse, "fasta")

    print('Done, see output in "{}"'.format(args.outdir))


# --------------------------------------------------
if __name__ == '__main__':
    main()

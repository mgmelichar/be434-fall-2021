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

    os.mkdir(os.path.join(os.getcwd(), args.outdir))

    even_seq = []
    odd_seq = []

    for file in args.FILE:
        root, ext = os.path.splitext(os.path.basename(file.name))
        i = 0
        for record in SeqIO.parse(file, "fasta"):
            i += 1
            if (i % 2) == 0:
                even_seq.append(record)
            else:
                odd_seq.append(record)

        SeqIO.write(even_seq, "{}".format(
            os.path.join(args.outdir, root+"_2"+ext)), "fasta")
        SeqIO.write(odd_seq, "{}".format(
            os.path.join(args.outdir, root+"_1"+ext)), "fasta")

    print('Done, see output in "{}"'.format(args.outdir))


# --------------------------------------------------
if __name__ == '__main__':
    main()

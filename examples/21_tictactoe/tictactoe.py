#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-11-08
Purpose: Rock the Casbah
"""

import argparse
from tabulate import tabulate

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='The state of the board',
                        metavar='board',
                        type=str,
                        default=range(1, 10))

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        choices='XO',
                        metavar='player',
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell 1-9',
                        metavar='cell',
                        type=int,
                        choices=range(1, 10),
                        default=None)
    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    board = list(args.board)

    if args.player and args.cell:
        board[args.cell - 1] = args.player

    print(makeboard(board))

# --------------------------------------------------
def makeboard(board_list):

    cell_inputs= [board_list[0:3], board_list[3:6], board_list[6:9]]

    return tabulate(cell_inputs, tablefmt='grid')


# --------------------------------------------------
if __name__ == '__main__':
    main()

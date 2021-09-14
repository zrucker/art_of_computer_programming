#!/usr/bin/env python3
"""
Date   : 2021-09-13
Purpose: Euclid's algorithm
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Euclid\'s algorithm',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('digits',
                        metavar='int',
                        nargs=2,
                        help='Integers to factor')

    return parser.parse_args()


# --------------------------------------------------
def reduce(m, n, r):
    """reduce for the next round"""
    m = n
    n = r
    return m, n, r


# --------------------------------------------------
def find_remainder(m, n, r):
    """calculate the remainder"""
    r = m % n
    return r


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    nums = args.digits
    solution = ''
    m, n, r = int(nums[0]), int(nums[1]), -1

    """Ensure m is greater than or equal to n"""
    if m < n:
        n = m

    """Find remainder"""
    while r != 0:
        r = find_remainder(m, n, r)
        solution = n
        m, n, r, = reduce(m, n, r)

    print("The solution is {}.".format(solution))


# --------------------------------------------------
if __name__ == '__main__':
    main()

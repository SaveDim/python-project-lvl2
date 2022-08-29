#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Gendiff script."""

import argparse
from gendiff.generate_diff import generate_diff


def main():
    """Will show diff between two files."""
    parser = argparse.ArgumentParser(
        description='Compares two configuration'
                    'files and shows a difference.')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument(
                        '-f', '--format', action='store',
                        help='set format of output'
                        )
    parser.parse_args()
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()

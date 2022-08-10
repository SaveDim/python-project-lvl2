#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Gendiff script."""

import argparse


def main():
    """Will show diff between two files."""
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    args = parser.parse_args()

if __name__ == '__main__':
    main()
import argparse

parser = argparse.ArgumentParser(prog='gendiff',
                                 description='Compares two configuration files,'
                                             'and shows a difference.')
parser.add_argument('first_file second_file')
parser.add_argument('first_file', nargs='+', help='second_file')

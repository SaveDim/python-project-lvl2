"""Generate_diff logic."""

from gendiff.formatters.getting_format import choose_format

from .data_parser import get_file_data
from .gen_dict_diff import dict_differencer


def generate_diff(file_path1, file_path2, format='stylish'):
    """Return difference between file_path1 and file_path2."""
    file1 = get_file_data(file_path1)
    file2 = get_file_data(file_path2)
    diff = dict_differencer(file1, file2)
    return choose_format(diff, format)

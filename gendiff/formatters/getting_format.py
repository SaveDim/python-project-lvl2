from gendiff.formatters.stylish import stylish
from gendiff.formatters.json import get_json


def choose_format(diff_list, format):
    if format == 'stylish':
        return stylish(diff_list)
    elif format == 'json':
        return get_json(diff_list)

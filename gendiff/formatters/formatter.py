"""Choose file format."""

from gendiff.formatters.json import get_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def choose_format(diff_list, format):
    """Return data of choosen file format."""
    if format == 'stylish':
        return stylish(diff_list)
    elif format == 'json':
        return get_json(diff_list)
    elif format == 'plain':
        return plain(diff_list)

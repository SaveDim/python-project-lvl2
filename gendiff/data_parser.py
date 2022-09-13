"""Parse data within .json, .yaml and .yml files."""

import json
from pathlib import Path

import yaml


def get_file_data(path_to_file):
    format = get_extention(path_to_file)
    file_data = load_file_data(open_file(path_to_file), format)
    return file_data


def get_extention(path_to_file):
    extention = Path(path_to_file).suffix
    if extention.lower() == '.json':
        return 'json'
    elif extention == '.yaml' or extention == '.yml':
        return 'yaml'


def open_file(fielname):
    return open(fielname)


def load_file_data(filename, format):
    if format == 'json':
        return json.load(filename)
    elif format == 'yaml':
        return yaml.safe_load(filename)

"""Parse data within .json, .yaml, .yml files"""

import json
import yaml


def get_file_data(path_to_file):
    if path_to_file.endswith('.json'):
        file_data = json.load(open(path_to_file))
    elif path_to_file.endswith('.yaml') or path_to_file.endswith('.yml'):
        file_data = yaml.safe_load(open(path_to_file))
    return file_data

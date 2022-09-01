"""Generate_diff logic."""

import json


def open_file(file_path1, file_path2):
    with open(file_path1, 'r') as file1:
        file1 = json.load(file1)
    with open(file_path2, 'r') as file2:
        file2 = json.load(file2)
    return file1, file2


def generate_diff(file_path1, file_path2):
    """Return difference between file_path1 and file_path2."""
    file1, file2 = open_file(file_path1, file_path2)
    diff = '{\n'
    keys_file1, keys_file2 = list(file1.keys()), list(file2.keys())
    for key in sorted(keys_file1):
        file1_value = str(file1[key]).lower()
        if key not in keys_file2:
            diff += f'  - {key}: {file1_value}\n'
        elif key in keys_file2 and file1[key] == file2[key]:
            diff += f'    {key}: {file1_value}\n'
        elif key in keys_file2 and file1[key] != file2[key]:
            diff += f'  - {key}: {file1_value}\n' \
                      f'  + {key}: {str(file2[key]).lower()}\n'
    for key in keys_file2:
        if key not in keys_file1:
            diff += f'  + {key}: {str(file2[key]).lower()}\n'
    diff += '}'
    return diff

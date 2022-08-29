"""Generate_diff logic."""

import json


def generate_diff(file_path1, file_path2):
    """Return difference between file_path1 and file_path2."""
    with open(file_path1, 'r') as file1:
        file1 = json.load(file1)
    with open(file_path2, 'r') as file2:
        file2 = json.load(file2)
    result = '{\n'
    keys_file1, keys_file2 = list(file1.keys()), list(file2.keys())
    for i in sorted(keys_file1):
        if i not in keys_file2:
            result += '  - ' + str(i) + ': ' + str(file1[i]).lower() + '\n'
        elif i in keys_file2 and file1[i] == file2[i]:
            result += '    ' + str(i) + ': ' + str(file1[i]).lower() + '\n'
        elif i in keys_file2 and file1[i] != file2[i]:
            result += '  - ' + str(i) + ': ' + str(file1[i]).lower() + '\n'
            result += '  + ' + str(i) + ': ' + str(file2[i]).lower() + '\n'
    for i in keys_file2:
        if i not in keys_file1:
            result += '  + ' + str(i) + ': ' + str(file2[i]).lower() + '\n'
    result += '}'
    return result

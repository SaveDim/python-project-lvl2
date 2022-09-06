"""Generate_diff logic."""

from data_parser import get_file_data


def generate_diff(file_path1, file_path2):
    """Return difference between file_path1 and file_path2."""
    file1 = get_file_data(file_path1)
    file2 = get_file_data(file_path2)
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

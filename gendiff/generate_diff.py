import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1:
        a = json.load(file1)
    with open(file_path2, 'r') as file2:
        b = json.load(file2)
    result = '{\n'
    keys_file1, keys_file2 = list(a.keys()), list(b.keys())
    for i in sorted(keys_file1):
        if i not in keys_file2:
            result += '  - ' + str(i) + ': ' + str(a[i]).lower() + '\n'
        elif i in keys_file2 and a[i] == b[i]:
            result += '    ' + str(i) + ': ' + str(a[i]).lower() + '\n'
        elif i in keys_file2 and a[i] != b[i]:
            result += '  - ' + str(i) + ': ' + str(a[i]).lower() + '\n'
            result += '  + ' + str(i) + ': ' + str(b[i]).lower() + '\n'
    for i in keys_file2:
        if i not in keys_file1:
            result += '  + ' + str(i) + ': ' + str(b[i]).lower() + '\n'
    return result + '}'

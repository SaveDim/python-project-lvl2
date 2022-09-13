def stylish(diff_list, level=0):
    """Returns string in required format."""
    result = '{\n'
    indent = '  '

    for i in range(level):
        indent += '    '

    diff_list.sort(key=lambda x: x['name'])

    for node in diff_list:
        if node['status'] == 'nested':
            data = stylish(node['children'], level + 1)
            result += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'not changed':
            data = get_string(node['data'], indent)
            result += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'added':
            data = get_string(node['data'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
        if node['status'] == 'deleted':
            data = get_string(node['data'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
        if node['status'] == 'changed':
            data = get_string(node['data before'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
            data = get_string(node['data after'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
    result += indent[:-2] + '}'

    return result


def get_string(data, indent):
    """Returns booleans as lower string format."""
    if type(data) is dict:
        indent += '    '
        result = '{\n'
        for key in data.keys():
            value = get_string(data[key], indent)
            result += indent + '  ' + key + ': ' + value + '\n'
        result += indent[:-2] + '}'
    elif data is None:
        result = 'null'
    else:
        result = str(data).lower()

    return result

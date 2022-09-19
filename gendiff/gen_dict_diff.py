"""Find difference between two dictionaries."""


def build_diff(dict1, dict2):
    result = []
    keys = sorted(dict1.keys() | dict2.keys())

    for key in keys:
        node = {'name': key}
        if key not in dict1:
            node['status'] = 'added'
            node['data'] = dict2[key]
        elif key not in dict2:
            node['status'] = 'deleted'
            node['data'] = dict1[key]
        elif type(dict1[key]) is dict and type(dict2[key]) is dict:
            node['status'] = 'nested'
            node['children'] = build_diff(dict1[key], dict2[key])
        elif dict1[key] == dict2[key]:
            node['status'] = 'not changed'
            node['data'] = dict1[key]
        else:
            node['status'] = 'changed'
            node['data_before'] = dict1[key]
            node['data_after'] = dict2[key]
        result.append(node)

    return result

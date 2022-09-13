import json


def get_json(diff_list):
    return json.dumps(diff_list, indent=4)

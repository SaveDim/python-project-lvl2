"""Return data from .json."""

import json


def get_json(diff_list):
    """Returns json dict."""
    return json.dumps(diff_list, indent=4)

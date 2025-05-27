import json

import yaml


def get_parser(suffix_path_before, suffix_path_after):
    if suffix_path_before != suffix_path_after:
        raise Exception('File formats must be the same')

    parsers = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }

    return parsers[suffix_path_before]
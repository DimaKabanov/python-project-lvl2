from pathlib import Path

from gendiff.formatters.main import get_formatter
from gendiff.parsers import get_parser

properties = [
    {
        'type': 'added',
        'check': lambda data: data['key'] not in data['data_before'],
        'extend': lambda data: {'new_value': data['value_after']}
    },
    {
        'type': 'deleted',
        'check': lambda data: data['key'] not in data['data_after'],
        'extend': lambda data: {'old_value': data['value_before']}
    },
    {
        'type': 'complex',
        'check': lambda data: (
            isinstance(data['value_before'], dict) and
            isinstance(data['value_after'], dict)
        ),
        'extend': lambda data: {
            'children': data['make_ast'](
                data['value_before'],
                data['value_after']
            )
        }
    },
    {
        'type': 'unchanged',
        'check': lambda data: data['value_before'] == data['value_after'],
        'extend': lambda data: {'old_value': data['value_before']}
    },
    {
        'type': 'changed',
        'check': lambda data: data['value_before'] != data['value_after'],
        'extend': lambda data: {
            'old_value': data['value_before'],
            'new_value': data['value_after']
        }
    },
]


def make_ast(data_before, data_after):
    keys = sorted(list(set(data_before) | set(data_after)))

    def find_property(key):
        data = {
            'data_before': data_before,
            'data_after': data_after,
            'value_before': data_before.get(key),
            'value_after': data_after.get(key),
            'key': key,
            'make_ast': make_ast,
        }

        return next(
            {
                'type': prop['type'],
                'key': key,
                **prop['extend'](data)
            }
            for prop in properties
            if prop['check'](data)
        )

    return list(map(find_property, keys))


def generate_diff(
        path_to_file_before,
        path_to_file_after,
        format_name='stylish'
):
    suffix_path_before = Path(path_to_file_before).suffix
    suffix_path_after = Path(path_to_file_after).suffix

    parse_file = get_parser(suffix_path_before, suffix_path_after)

    data_file_before = open(path_to_file_before)
    data_file_after = open(path_to_file_after)

    parsed_file_before = parse_file(data_file_before)
    parsed_file_after = parse_file(data_file_after)

    ast = make_ast(parsed_file_before, parsed_file_after)

    format_diff = get_formatter(format_name)
    formatted_diff = format_diff(ast)

    return formatted_diff

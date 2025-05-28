from gendiff.utils import flatten


def format_value(value):
    match value:
        case None:
            return 'null'
        case bool():
            return str(value).lower()
        case str():
            return f"'{value}'"
        case dict():
            return '[complex value]'
        case _:
            return value


def format_plain(ast):
    def format_node(node, keys=[]):
        new_value = node.get('new_value')
        old_value = node.get('old_value')
        children = node.get('children')

        new_keys = [*keys, node['key']]
        path = '.'.join(new_keys)

        match node['type']:
            case 'added':
                value = format_value(new_value)
                return f"Property '{path}' was added with value: {value}"
            case 'deleted':
                return f"Property '{path}' was removed"
            case 'changed':
                first_value = format_value(old_value)
                second_value = format_value(new_value)
                return (f"Property '{path}' was updated. "
                        f"From {first_value} to {second_value}")
            case 'unchanged':
                return []
            case 'complex':
                return list(map(
                    lambda child: format_node(child, new_keys),
                    children
                ))

    return '\n'.join(flatten(map(format_node, ast)))
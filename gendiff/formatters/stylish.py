from gendiff.utils import flatten


def wrap_items(nodes, depth=0):
    return f"{{\n{'\n'.join(flatten(nodes))}\n{get_indent(depth)}}}"


def get_indent(depth, sign=' '):
    if depth == 0:
        return ''

    spaces = '    ' * depth
    return f'{spaces[:-2]}{sign}{spaces[-1]}'


def format_value(value, depth):
    match value:
        case None:
            return 'null'
        case bool():
            return str(value).lower()
        case dict():
            indent = get_indent(depth + 1)
            formatted_items = map(
                lambda key: (
                    f'{indent}{key}: {format_value(value[key], depth + 1)}'
                ),
                value.keys()
            )
            return wrap_items(formatted_items, depth)
        case _:
            return value


def format_stylish(ast):
    def format_node(node, depth=1):
        key = node['key']
        new_value = node.get('new_value')
        old_value = node.get('old_value')
        children = node.get('children')

        match node['type']:
            case 'added':
                indent = get_indent(depth, '+')
                value = format_value(new_value, depth)
                return f"{indent}{key}: {value}"
            case 'deleted':
                indent = get_indent(depth, '-')
                value = format_value(old_value, depth)
                return f"{indent}{key}: {value}"
            case 'changed':
                first_indent = get_indent(depth, '-')
                second_indent = get_indent(depth, '+')
                first_value = format_value(old_value, depth)
                second_value = format_value(new_value, depth)
                return [
                    f"{first_indent}{key}: {first_value}",
                    f"{second_indent}{key}: {second_value}"
                ]
            case 'unchanged':
                indent = get_indent(depth)
                value = format_value(old_value, depth)
                return f"{indent}{key}: {value}"
            case 'complex':
                indent = get_indent(depth)
                formatted_children = map(
                    lambda child: format_node(child, depth + 1),
                    children
                )
                wrapped_children = wrap_items(formatted_children, depth)
                return f"{indent}{key}: {wrapped_children}"

    return wrap_items(map(format_node, ast))
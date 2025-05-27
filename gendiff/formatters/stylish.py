from gendiff.utils import flatten


def get_indent(depth, sign=' '):
    if depth == 0:
        return ''

    spaces = '    ' * depth
    return f'{spaces[:-2]}{sign}{spaces[-1]}'


def value_to_string(node, depth):
    match node:
        case None:
            return 'null'
        case bool():
            return str(node).lower()
        case dict():
            formatted_items = map(
                lambda key: f'{get_indent(depth + 1)}{key}: {value_to_string(node[key], depth + 1)}',
                node.keys()
            )
            return f"{{\n{'\n'.join(formatted_items)}\n{get_indent(depth)}}}"
        case _:
            return str(node)


def format_stylish(ast, current_depth=0):
    def format_node_by_type(node):
        depth = node['depth']
        key = node['key']

        match node['type']:
            case 'added':
                indent = get_indent(depth, '+')
                value = value_to_string(node['new_value'], depth)
                return f"{indent}{key}: {value}"
            case 'deleted':
                indent = get_indent(depth, '-')
                value = value_to_string(node['old_value'], depth)
                return f"{indent}{key}: {value}"
            case 'changed':
                first_indent = get_indent(depth, '-')
                second_indent = get_indent(depth, '+')
                old_value = value_to_string(node['old_value'], depth)
                new_value = value_to_string(node['new_value'], depth)
                return [
                    f"{first_indent}{key}: {old_value}",
                    f"{second_indent}{key}: {new_value}"
                ]
            case 'unchanged':
                indent = get_indent(depth)
                value = value_to_string(node['old_value'], depth)
                return f"{indent}{key}: {value}"
            case 'complex':
                indent = get_indent(depth)
                return f"{indent}{key}: {format_stylish(node['children'], depth)}"

    formatted_nodes = flatten(map(format_node_by_type, ast))
    return f"{{\n{'\n'.join(formatted_nodes)}\n{get_indent(current_depth)}}}"
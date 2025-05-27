def value_to_str(value):
    match value:
        case None:
            return 'null'
        case bool():
            return str(value).lower()
        case _:
            return str(value)


def format_plain(ast):
    def format_node_by_type(node):
        key = node['key']

        match node['type']:
            case 'added':
                value = value_to_str(node['new_value'])
                return f"Property '{key}' was added with value: {value}"
            case 'deleted':
                return f"Property '{key}' was removed"
            case 'changed':
                old_value = value_to_str(node['old_value'])
                new_value = value_to_str(node['new_value'])
                result = f"From {old_value} to {new_value}"
                return f"Property '{key}' was updated. {result}"
            
    without_unchanged = filter(lambda node: node['type'] != 'unchanged', ast)
    formatted_nodes = map(format_node_by_type, without_unchanged)
    
    return '\n'.join(formatted_nodes)
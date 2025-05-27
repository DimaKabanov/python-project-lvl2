from gendiff.formatters.stylish import format_stylish


def get_formatter(format_name):
    formatters = {
        'stylish': format_stylish,
    }

    return formatters[format_name]
from pathlib import Path

from gendiff.parser import get_parser


def plain_format(before, after, keys):
    result = []

    for key in keys:
        if key in before and key not in after:
            result.append(f"  - {key}: {before[key]}")
        elif key not in before and key in after:
            result.append(f"  + {key}: {after[key]}")
        elif key in before and key in after and (before[key] == after[key]):
            result.append(f"    {key}: {before[key]}")
        else:
            result.append(f"  - {key}: {before[key]}")
            result.append(f"  + {key}: {after[key]}")

    return f"{{\n{'\n'.join(map(str.lower, result))}\n}}"


def generate_diff(path_to_file_before, path_to_file_after):
    suffix_path_before = Path(path_to_file_before).suffix
    suffix_path_after = Path(path_to_file_after).suffix

    parse_file = get_parser(suffix_path_before, suffix_path_after)

    parsed_file_before = parse_file(open(path_to_file_before))
    parsed_file_after = parse_file(open(path_to_file_after))

    keys = sorted(list(set(parsed_file_before) | set(parsed_file_after)))
    diff = plain_format(parsed_file_before, parsed_file_after, keys)

    return diff

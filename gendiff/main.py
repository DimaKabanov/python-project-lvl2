import json


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
    data_file_before = json.load(open(path_to_file_before))
    data_file_after = json.load(open(path_to_file_after))

    keys = sorted(list(set(data_file_before) | set(data_file_after)))
    diff = plain_format(data_file_before, data_file_after, keys)

    return diff

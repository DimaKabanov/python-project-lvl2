import json


def generate_diff(path_to_file_before, path_to_file_after):
    data_file_before = json.load(open(path_to_file_before))
    data_file_after = json.load(open(path_to_file_after))

    print(data_file_before)
    print(data_file_after)
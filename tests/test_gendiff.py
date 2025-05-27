from pathlib import Path

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_flat_json_stylish_diff():
    before_path = get_test_data_path('before.json')
    after_path = get_test_data_path('after.json')

    actual = generate_diff(before_path, after_path)
    expected = read_file('output.txt')

    assert actual == expected


def test_flat_yml_stylish_diff():
    before_path = get_test_data_path('before.yml')
    after_path = get_test_data_path('after.yml')

    actual = generate_diff(before_path, after_path)
    expected = read_file('output.txt')

    assert actual == expected


def test_nested_json_stylish_diff():
    before_path = get_test_data_path('before-nested.json')
    after_path = get_test_data_path('after-nested.json')

    actual = generate_diff(before_path, after_path)
    expected = read_file('output-nested.txt')

    assert actual == expected


def test_nested_yml_stylish_diff():
    before_path = get_test_data_path('before-nested.yml')
    after_path = get_test_data_path('after-nested.yml')

    actual = generate_diff(before_path, after_path)
    expected = read_file('output-nested.txt')

    assert actual == expected


def test_flat_json_plain_diff():
    before_path = get_test_data_path('before.json')
    after_path = get_test_data_path('after.json')

    actual = generate_diff(before_path, after_path, format_name='plain')
    expected = read_file('output-plain.txt')

    assert actual == expected


def test_flat_yml_plain_diff():
    before_path = get_test_data_path('before.yml')
    after_path = get_test_data_path('after.yml')

    actual = generate_diff(before_path, after_path, format_name='plain')
    expected = read_file('output-plain.txt')

    assert actual == expected
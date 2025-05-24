from pathlib import Path

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_flat_json_diff():
    before_path = get_test_data_path('before.json')
    after_path = get_test_data_path('after.json')

    actual = generate_diff(before_path, after_path)
    expected = read_file('output.txt')

    assert actual == expected


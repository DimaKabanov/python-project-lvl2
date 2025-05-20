import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.parse_args()


if __name__ == "__main__":
    main()
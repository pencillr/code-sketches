import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Default.')
    parser.add_argument('--param', help='an integer for the accumulator')
    return parser.parse_args()


def main():
    args = parse_arguments()
    return args


if __name__ == '__main__':
    main()
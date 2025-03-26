import sys


def main():
    """Script entry point."""

    alphabet = "".join([chr(c) for c in range(ord("a"), ord("z") + 1)])
    print(alphabet if sys.argv[0].endswith("a-z.py") else alphabet[::-1])


if __name__ == '__main__':
    main()

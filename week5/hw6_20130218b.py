def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """Returns the characters from the 'text' argument that 'chars' argument also includes, as a string."""

    return "".join([c for c in text if c in chars])


def main():
    """Script entry point."""

    print(f"{valid("Barking!")=}")
    print(f"{valid("KL754", "0123456789")=}")
    print(f"{valid("BEAN", "abcdefghijklmnopqrstuvwxyz")=}")


if __name__ == '__main__':
    main()

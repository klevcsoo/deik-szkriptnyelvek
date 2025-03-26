def main():
    """Script entry point."""

    reference_character = "ő"
    print("".join([chr(ord(reference_character) - ord(c)) for c in ["ğ", "ġ", "ğ", "Ĝ"]]))


if __name__ == '__main__':
    main()

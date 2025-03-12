def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def main():
    s = "anna"
    print(is_palindrome(s))


if __name__ == "__main__":
    main()

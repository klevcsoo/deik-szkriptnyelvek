def solution1(input: str):
    return input == input[::-1]


def solution2(input: str):
    left = 0
    right = len(input) - 1

    while left < right:
        if input[left] != input[right]:
            return False
        left += 1
        right -= 1

    return True


def solution3(input: str):
    if len(input) <= 1:
        return True
    if input[0] != input[-1]:
        return False
    return solution3(input[1:-1])


def main():
    word_palindrome = "hannah"
    print(f"{word_palindrome=}")
    print(f"{solution1(word_palindrome)=}")
    print(f"{solution2(word_palindrome)=}")
    print(f"{solution3(word_palindrome)=}")

    print()

    word_non_palindrome = "steven"
    print(f"{word_non_palindrome=}")
    print(f"{solution1(word_non_palindrome)=}")
    print(f"{solution2(word_non_palindrome)=}")
    print(f"{solution3(word_non_palindrome)=}")


if __name__ == '__main__':
    main()

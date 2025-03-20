# 20120818f


def square_diff(n: int) -> int:
    square_sum = sum([i ** 2 for i in range(1, n + 1)])
    sum_of_squares = sum(range(1, n + 1)) ** 2
    return abs(square_sum - sum_of_squares)


def main():
    print(f"{square_diff(100)=}")


if __name__ == '__main__':
    main()

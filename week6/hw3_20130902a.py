def median(vector: list[int]) -> float:
    """Calculates the median of a list of integers."""

    sorted_vector = sorted(vector)
    middle_index = len(sorted_vector) // 2

    if len(sorted_vector) % 2 != 0:
        return sorted_vector[middle_index]
    else:
        return (sorted_vector[middle_index] + sorted_vector[middle_index - 1]) / 2


def main():
    """Script entry point."""

    print(f"{median([1, 2, 3, 4, 5])=}")
    print(f"{median([3, 1, 2, 5, 3])=}")
    print(f"{median([1, 300, 2, 200, 1])=}")
    print(f"{median([3, 6, 20, 99, 10, 15])=}")


if __name__ == '__main__':
    main()

def print_munchausen_numbers_up_to(limit: int):
    """Prints all the Münchausen numbers from 0 (inclusive), up to the specified limit (exclusive)."""

    for n in range(0, limit):
        print(f"\033[0;37m{n}\033[0m", end="\r")
        n_sum = sum([int(nc) ** int(nc) for nc in list(str(n))])
        if n == 0 or n == n_sum:
            print(n)


def main():
    """Script entry point."""

    print_munchausen_numbers_up_to(440000000)


if __name__ == '__main__':
    main()

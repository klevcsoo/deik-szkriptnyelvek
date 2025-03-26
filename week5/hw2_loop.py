def loop(n: int, debug: bool = False) -> None:
    if debug:
        print("#start loop")

    print(" ".join([str(n) for n in range(1, n + 1)]))

    if debug:
        print("#end loop")


def main():
    loop(5)

    print("\n----------\n")

    loop(5, debug=True)


if __name__ == '__main__':
    main()

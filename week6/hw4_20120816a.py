def draw_board(positions: list[int]):
    """Draws a chess board, with the Queens on their specified positions."""

    if len(positions) != 8:
        raise Exception("Length of 'positions' list must be 8.")

    print("+-----------------+")

    for y in range(8):
        print("| " + " ".join(["Q" if abs(positions[x] - 7) == y else "." for x in range(8)]) + " |")

    print("+-----------------+")


def main():
    """Script entry point."""

    draw_board([7, 3, 0, 2, 5, 1, 6, 4])

    print()

    draw_board([0, 4, 7, 5, 2, 6, 1, 3])


if __name__ == '__main__':
    main()

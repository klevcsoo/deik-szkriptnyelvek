# 20130211b

def draw_diamond(height: int) -> None:
    if height % 2 == 0:
        print("Error: Only odd heights are accepted.")
        return

    for i in range(height // 2 + 1):
        print(' ' * (height // 2 - i) + '*' * (2 * i + 1))

    for i in range(height // 2 - 1, -1, -1):
        print(' ' * (height // 2 - i) + '*' * (2 * i + 1))


def main():
    draw_diamond(3)
    print()
    draw_diamond(7)
    print()
    draw_diamond(4)


if __name__ == '__main__':
    main()

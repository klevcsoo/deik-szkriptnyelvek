N = 1000


def main():
    result = 0
    for n in range(1, N):
        if n % 3 == 0 or n % 5 == 0:
            result += n
    print(result)

    print(sum([n if n % 3 == 0 or n % 5 == 0 else 0 for n in range(1, N)]))


if __name__ == '__main__':
    main()

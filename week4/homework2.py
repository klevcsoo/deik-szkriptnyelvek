# 20121001b

def variation1():
    return sum(range(1, 101))


def variation2():
    return sum([sum([int(c) for c in str(i)]) for i in range(1, 101)])


def main():
    print(variation1())
    print(variation2())


if __name__ == '__main__':
    main()

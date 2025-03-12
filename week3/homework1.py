import random


def multiply_elements(input_array: list[int]):
    product = 1
    for element in input_array:
        product *= element
    return product


def main():
    print([])
    print(multiply_elements([]))

    print()

    array = [random.randint(1, 10) for i in range(0, 10)]
    print(array)
    print(multiply_elements(array))


if __name__ == '__main__':
    main()

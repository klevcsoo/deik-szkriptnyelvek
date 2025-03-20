# 20130305a

def xor(a: bool, b: bool) -> bool:
    return a or b and not (a and b)


def main():
    str1 = "python"
    str2 = None

    print(f"{bool(str1)=}")
    print(f"{bool(str2)=}")
    print(f"{xor(bool(str1), bool(str2))=}")


if __name__ == '__main__':
    main()

def main():
    li = ["alpha", "beta", "gamma"]

    for i in range(0, len(li)):
        print(f"{i + 1} -> {li[i]}")

    print("\n----------\n")

    for i, e in enumerate(li, start=1):
        print(f"{i} -> {e}")


if __name__ == '__main__':
    main()

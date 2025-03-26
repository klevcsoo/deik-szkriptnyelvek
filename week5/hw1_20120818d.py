def main():
    """Application entry point."""

    print(f"01 -> {[f"{s.upper()}!" for s in ["auto", "villamos", "metro"]]=}")

    print(f"02 -> {[s.capitalize() for s in ["aladar", "bela", "cecil"]]=}")

    print(f"03 -> {[0 for _n in range(0, 10)]=}")

    print(f"04 -> {[n * 2 for n in range(1, 11)]=}")

    print(f"05 -> {[int(s) for s in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']]=}")

    print(f"06 -> {[int(s) for s in "1234567"]=}")

    print(f"07 -> {[len(s) for s in "The quick brown fox jumps over the lazy dog".split()]=}")

    print(f"08 -> {[s[0] for s in "python is an awesome language".split(" ")]=}")

    print(f"09 -> {[(s, len(s)) for s in "The quick brown fox jumps over the lazy dog".split()]=}")

    print(f"10 -> {[n for n in range(0, 10) if n % 2 == 0]=}")

    print(f"11 -> {[n for n in [n**2 for n in range(0, 20)] if n % 2 == 0]=}")

    print(f"12 -> {[n for n in [n**2 for n in range(0, 20)] if str(n)[-1] == "4"]=}")

    print(f"13 -> {"".join([chr(n) for n in range(ord("A"), ord("Z") + 1)])=}")

    print(f"14 -> {[s.strip() for s in [' apple ', ' banana ', ' kiwi']]=}")

    print(f"15 -> {"".join([str(n) for n in [1, 0, 1, 1, 0, 1, 0, 0]])=}")


if __name__ == '__main__':
    main()

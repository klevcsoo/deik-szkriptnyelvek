def is_anagram1(s1: str, s2: str) -> bool:
    """Resolves whether a pair of strings are anagrams or not."""

    return "".join(sorted(list(s1.lower()))).strip() == "".join(sorted(list(s2.lower()))).strip()


def is_anagram2(*texts: str) -> bool:
    """Resolves whether a list of strings only contains anagrams or not."""
    return len(set(["".join(sorted(list(s.lower()))).strip() for s in texts])) == 1


def main():
    """Script entry point."""

    print(f"{is_anagram1("listen", "silent") = }")
    print(f"{is_anagram2("listen", "silent") = }")

    print()

    print(f"{is_anagram1("A gentleman", "Elegant man") = }")
    print(f"{is_anagram2("A gentleman", "Elegant man") = }")

    print()

    print(f"{is_anagram1("Clint Eastwood", "Old west action") = }")
    print(f"{is_anagram2("Clint Eastwood", "Old west action") = }")

    print()

    print(f"{is_anagram1("dormitory", "dirty room") = }")
    print(f"{is_anagram2("dormitory", "dirty room") = }")

    print()

    print(f"{is_anagram1("étel", "élet") = }")
    print(f"{is_anagram2("étel", "élet") = }")

    print()

    print(f"{is_anagram1("papi", "pipa") = }")
    print(f"{is_anagram2("papi", "pipa") = }")

    print()

    print(f"{is_anagram1("kolostor", "rostokol") = }")
    print(f"{is_anagram2("kolostor", "rostokol") = }")


if __name__ == '__main__':
    main()

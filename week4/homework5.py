# 20120910a


LOW_TONE_CHARACTERS = "aáoóuú"
HIGH_TONE_CHARACTERS = "eéiíöőüű"


def resolve_tone(word: str) -> str:
    has_low = True in [c in word for c in LOW_TONE_CHARACTERS]
    has_high = True in [c in word for c in HIGH_TONE_CHARACTERS]

    if has_low and has_high:
        return "vegyes"
    elif has_low and not has_high:
        return "mély"
    elif has_high and not has_low:
        return "magas"
    else:
        return "semmilyen"


def main():
    print(f"{resolve_tone("ablak")=}")
    print(f"{resolve_tone("erkély")=}")
    print(f"{resolve_tone("kisvasút")=}")
    print(f"{resolve_tone("magas")=}")
    print(f"{resolve_tone("mély")=}")
    print(f"{resolve_tone("Pfffffff")=}")


if __name__ == '__main__':
    main()

ENCODED_TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def decode(input: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_text = ""

    for char in input:
        if char.isalpha():  # ha betűről van szó, decódoljuk

            # találjuk meg a karakter megfelelőjét és toljuk a helyét kettővel
            index = alphabet.index(char.lower())
            decoded_char = alphabet[(index + 2) % 26]

            # ha az eredeti karakter nagybetű volt, legyen ez is az
            if char.isupper():
                decoded_char = decoded_char.upper()

            # adjuk hozzá a dekódolt szövegkez a karakterünket
            decoded_text += decoded_char
        else:  # ha nem betűról van szó, hagyjuk úgy
            decoded_text += char

    return decoded_text


def main():
    print(decode(ENCODED_TEXT))


if __name__ == '__main__':
    main()

import string


def clean_url(url: str):
    internal = url
    for char in string.whitespace:
        internal = internal.replace(char, "")
    return internal


def main():
    input_urls = ["192.20.246.138:\n 6666", "206.130.99.82:\n8080"]
    for url in input_urls:
        print(f"{url=}")
        print(f"{clean_url(url)=}")
        print()


if __name__ == '__main__':
    main()

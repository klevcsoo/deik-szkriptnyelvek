import os
import pathlib
import shutil

CLI_HEADER = """
---------------------------
Create an empty source file
---------------------------
"""

LANGUAGE_OPTIONS: list[tuple[str, str]] = [
    ("Python", "py"),
    ("C", "c"),
    ("C++", "cpp"),
    ("C#", "cs"),
    ("Go", "go"),
    ("Java", "java"),
    ("Kotlin", "kt"),
    ("Ruby", "rb"),
    ("Rust", "rs"),
    ("Scala", "scala")
]

TEMPLATE_FILE_NAME = "alap"


def print_language_options() -> None:
    """Prints the available language options."""
    max_name_length = max(len(name) for name, _ in LANGUAGE_OPTIONS)
    max_index_length = len(str(len(LANGUAGE_OPTIONS)))
    for index, (name, ext) in enumerate(LANGUAGE_OPTIONS, start=1):
        index_text = f"{(max_index_length - len(str(index))) * " "}{index}"
        name_text = f"{name}{(max_name_length - len(name)) * " "}"
        print(f"{index_text}) {name_text} [{ext}]")

    print(f"{(max_index_length - 1) * " "}q) quit")


def generate_language_file(language: tuple[str, str]) -> None:
    """Generates the template file for the chosen language."""

    template_path = pathlib.Path("", "templates", f"{TEMPLATE_FILE_NAME}.{language[1]}")
    output_path = pathlib.Path("", template_path.name)

    if not os.access(template_path, mode=os.R_OK):
        raise FileNotFoundError(f"Template file for {language[0]} could not be found at '{template_path.absolute()}'.")

    if os.access(output_path, mode=os.F_OK):
        raise FileExistsError(f"File '{output_path.absolute()}' already exists.")

    shutil.copy(template_path, output_path)

    print(f"Generated {language[0]} file at '{output_path.absolute()}'.")


def main() -> int:
    """Script entry point."""

    print(CLI_HEADER)
    print_language_options()

    prompt_input_value = input("> ")

    if prompt_input_value == "q":
        return 0

    try:
        chosen_option = LANGUAGE_OPTIONS[int(prompt_input_value) - 1]
        generate_language_file(chosen_option)
    except ValueError:
        print(f"[ERROR] Invalid option: '{prompt_input_value}'. Only the indexes of the listed options are accepted.")
        return 1
    except IndexError:
        print(f"[ERROR] Invalid option: '{prompt_input_value}'. Only the indexes of the listed options are accepted.")
        return 1
    except Exception as e:
        print(f"[ERROR] {e}")
        return 1

    return 0


if __name__ == '__main__':
    exit(main())

import sys

from nova.api import run_file

from nova.errors import (
    NovaError,
    LexerError,
    ParserError,
    RuntimeError,
    TypeError,
)


class Color:
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


def get_error_category(error):
    if isinstance(error, LexerError):
        return "Lexer Error"

    if isinstance(error, ParserError):
        return "Parser Error"

    if isinstance(error, TypeError):
        return "Type Error"

    if isinstance(error, RuntimeError):
        return "Runtime Error"

    return "Error"


def format_error(error, source, path):
    category = get_error_category(error)

    output = []

    output.append(f"{Color.BOLD}{Color.RED}{category}{Color.RESET}: {error.message}")

    if error.line is not None and error.column is not None:
        lines = source.splitlines()

        if 1 <= error.line <= len(lines):
            source_line = lines[error.line - 1]

            output.append("")

            output.append(
                f"{Color.CYAN}--> "
                f"{path}:{error.line}:{error.column}"
                f"{Color.RESET}"
            )

            output.append(f"{error.line} | {source_line}")

            output.append(
                " " * (len(str(error.line)) + 3 + error.column - 1)
                + f"{Color.YELLOW}^{Color.RESET}"
            )

    return "\n".join(output)


def main():
    if len(sys.argv) != 2:
        print("Usage: nova <file.nova>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        _, output = run_file(path)

        for line in output:
            print(line)

    except NovaError as error:
        with open(path, "r", encoding="utf-8") as file:
            source = file.read()

        print(
            format_error(
                error,
                source,
                path,
            )
        )

        sys.exit(1)


if __name__ == "__main__":
    main()

import sys

from nova.lexer.lexer import Lexer
from nova.parser.parser import Parser
from nova.interpreter.interpreter import Interpreter

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

    output.append(
        f"{Color.BOLD}{Color.RED}{category}{Color.RESET}: " f"{error.message}"
    )

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


def run_file(path):
    with open(path, "r", encoding="utf-8") as file:
        source = file.read()

    try:
        lexer = Lexer(source)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        ast = parser.parse()

        interpreter = Interpreter()
        interpreter.interpret(ast)

    except NovaError as error:
        print(
            format_error(
                error,
                source,
                path,
            )
        )

        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: nova <file.nova>")
        sys.exit(1)

    run_file(sys.argv[1])


if __name__ == "__main__":
    main()

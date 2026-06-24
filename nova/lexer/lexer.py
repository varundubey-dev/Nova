from nova.lexer.token import Token
from nova.lexer.token_types import TokenType

from nova.errors import (
    InvalidFloatLiteralError,
    UnterminatedStringError,
    UnterminatedCommentError,
    UnexpectedCharacterError,
)

KEYWORDS = {
    "print": TokenType.PRINT,
    "if": TokenType.IF,
    "else": TokenType.ELSE,

    "while": TokenType.WHILE,
    "for": TokenType.FOR,
    "in": TokenType.IN,

    "break": TokenType.BREAK,
    "continue": TokenType.CONTINUE,

    "true": TokenType.BOOLEAN,
    "false": TokenType.BOOLEAN,
    "null": TokenType.NULL,
}

TYPES = {"S", "N", "B", "U", "M"}


class Lexer:
    def __init__(self, source: str):
        self.source = source

        self.position = 0

        self.line = 1
        self.column = 1

        self.current_char = source[0] if source else None

    def advance(self):
        if self.current_char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        self.position += 1

        if self.position >= len(self.source):
            self.current_char = None
        else:
            self.current_char = self.source[self.position]

    def peek(self):
        next_position = self.position + 1

        if next_position >= len(self.source):
            return None

        return self.source[next_position]

    def peek_two(self):
        next_position = self.position + 2

        if next_position >= len(self.source):
            return None

        return self.source[next_position]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char in " \t\r":
            self.advance()

    def read_identifier(self):
        start_line = self.line
        start_column = self.column

        value = ""

        while self.current_char is not None and (
            self.current_char.isalnum() or self.current_char == "_"
        ):
            value += self.current_char
            self.advance()

        if value == "true":
            return Token(TokenType.BOOLEAN, True, start_line, start_column)

        if value == "false":
            return Token(TokenType.BOOLEAN, False, start_line, start_column)

        if value == "null":
            return Token(TokenType.NULL, None, start_line, start_column)

        if value in KEYWORDS:
            return Token(KEYWORDS[value], value, start_line, start_column)

        if value in TYPES:
            return Token(TokenType.TYPE, value, start_line, start_column)

        return Token(TokenType.IDENTIFIER, value, start_line, start_column)

    def read_number(self):
        start_line = self.line
        start_column = self.column

        value = ""

        while self.current_char is not None and self.current_char.isdigit():
            value += self.current_char
            self.advance()

        next_char = self.peek()

        if self.current_char == ".":

            if next_char is not None and next_char.isdigit():
                value += self.current_char
                self.advance()

                while self.current_char is not None and self.current_char.isdigit():
                    value += self.current_char
                    self.advance()

            elif next_char != ".":
                raise InvalidFloatLiteralError(
                    "Invalid float literal.",
                    self.line,
                    self.column,
                )

        if "." in value:
            value = float(value)
        else:
            value = int(value)

        return Token(
            TokenType.NUMBER,
            value,
            start_line,
            start_column,
        )

    def read_string(self):
        start_line = self.line
        start_column = self.column

        value = ""

        self.advance()

        while self.current_char is not None and self.current_char != '"':
            value += self.current_char
            self.advance()

        if self.current_char is None:
            raise UnterminatedStringError(
                "Unterminated string.",
                start_line,
                start_column,
            )

        self.advance()

        return Token(TokenType.STRING, value, start_line, start_column)

    def skip_single_line_comment(self):
        while self.current_char is not None and self.current_char != "\n":
            self.advance()

    def skip_multi_line_comment(self):
        self.advance()  # /
        self.advance()  # *

        while self.current_char is not None:
            if self.current_char == "*" and self.peek() == "/":
                self.advance()
                self.advance()
                return

            self.advance()

        raise UnterminatedCommentError(
            "Unterminated multi-line comment.",
            self.line,
            self.column,
        )

    def next_token(self):
        while self.current_char is not None:

            if self.current_char in " \t\r":
                self.skip_whitespace()
                continue

            if self.current_char == "\n":
                token = Token(TokenType.NEWLINE, "\\n", self.line, self.column)
                self.advance()
                return token

            if self.current_char == "/" and self.peek() == "/":
                self.skip_single_line_comment()
                continue

            if self.current_char == "/" and self.peek() == "*":
                self.skip_multi_line_comment()
                continue

            if self.current_char.isalpha() or self.current_char == "_":
                return self.read_identifier()

            if self.current_char.isdigit():
                return self.read_number()

            if self.current_char == '"':
                return self.read_string()

            line = self.line
            column = self.column

            # =====================
            # Two-character tokens
            # =====================

            if self.current_char == "=" and self.peek() == "=":
                self.advance()
                self.advance()
                return Token(TokenType.EQUAL_EQUAL, "==", line, column)

            if self.current_char == "!" and self.peek() == "=":
                self.advance()
                self.advance()
                return Token(TokenType.NOT_EQUAL, "!=", line, column)

            if self.current_char == "<" and self.peek() == "=":
                self.advance()
                self.advance()
                return Token(TokenType.LESS_EQUAL, "<=", line, column)

            if self.current_char == ">" and self.peek() == "=":
                self.advance()
                self.advance()
                return Token(TokenType.GREATER_EQUAL, ">=", line, column)

            if self.current_char == "&" and self.peek() == "&":
                self.advance()
                self.advance()
                return Token(TokenType.AND, "&&", line, column)

            if self.current_char == "|" and self.peek() == "|":
                self.advance()
                self.advance()
                return Token(TokenType.OR, "||", line, column)

            if self.current_char == ":" and self.peek() == ":":
                self.advance()
                self.advance()
                return Token(TokenType.DOUBLE_COLON, "::", line, column)

            if (
                self.current_char == "."
                and self.peek() == "."
                and self.peek_two() == "."
            ):
                self.advance()
                self.advance()
                self.advance()

                return Token(
                    TokenType.RANGE_INCLUSIVE,
                    "...",
                    line,
                    column,
                )

            if self.current_char == "." and self.peek() == ".":
                self.advance()
                self.advance()

                return Token(
                    TokenType.RANGE_EXCLUSIVE,
                    "..",
                    line,
                    column,
                )

            # =====================
            # One-character tokens
            # =====================

            if self.current_char == "+":
                self.advance()
                return Token(TokenType.PLUS, "+", line, column)

            if self.current_char == "-":
                self.advance()
                return Token(TokenType.MINUS, "-", line, column)

            if self.current_char == "*":
                self.advance()
                return Token(TokenType.STAR, "*", line, column)

            if self.current_char == "/":
                self.advance()
                return Token(TokenType.SLASH, "/", line, column)

            if self.current_char == "%":
                self.advance()
                return Token(TokenType.MODULO, "%", line, column)

            if self.current_char == "<":
                self.advance()
                return Token(TokenType.LESS, "<", line, column)

            if self.current_char == ">":
                self.advance()
                return Token(TokenType.GREATER, ">", line, column)

            if self.current_char == "!":
                self.advance()
                return Token(TokenType.NOT, "!", line, column)

            if self.current_char == ":":
                self.advance()
                return Token(TokenType.COLON, ":", line, column)

            if self.current_char == "=":
                self.advance()
                return Token(TokenType.EQUALS, "=", line, column)

            if self.current_char == "(":
                self.advance()
                return Token(TokenType.LPAREN, "(", line, column)

            if self.current_char == ")":
                self.advance()
                return Token(TokenType.RPAREN, ")", line, column)

            if self.current_char == "[":
                self.advance()
                return Token(TokenType.LBRACKET, "[", line, column)

            if self.current_char == "]":
                self.advance()
                return Token(TokenType.RBRACKET, "]", line, column)

            if self.current_char == "{":
                self.advance()
                return Token(TokenType.LBRACE, "{", line, column)

            if self.current_char == "}":
                self.advance()
                return Token(TokenType.RBRACE, "}", line, column)

            if self.current_char == ".":
                self.advance()
                return Token(TokenType.DOT, ".", line, column)

            if self.current_char == ",":
                self.advance()
                return Token(TokenType.COMMA, ",", line, column)

            if self.current_char == "?":
                self.advance()
                return Token(TokenType.QUESTION, "?", line, column)

            raise UnexpectedCharacterError(
                f"Unexpected character '{self.current_char}'.",
                line,
                column,
            )

        return Token(TokenType.EOF, None, self.line, self.column)

    def tokenize(self):
        tokens = []

        while True:
            token = self.next_token()
            tokens.append(token)

            if token.type == TokenType.EOF:
                break

        return tokens

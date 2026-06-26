from nova.lexer.token_types import TokenType


class Token:
    def __init__(
        self, token_type: TokenType, value=None, line: int = 1, column: int = 1
    ):
        self.type = token_type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return (
            f"Token("
            f"type={self.type.name}, "
            f"value={repr(self.value)}, "
            f"line={self.line}, "
            f"column={self.column}"
            f")"
        )

    def to_dict(self) -> dict[str, str | int | bool | None]:
        return {
            "type": self.type.name,
            "value": self.value,
            "line": self.line,
            "column": self.column,
        }

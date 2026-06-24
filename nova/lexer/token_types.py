from enum import Enum, auto


class TokenType(Enum):
    # Literals
    NUMBER = auto()
    STRING = auto()
    BOOLEAN = auto()
    NULL = auto()

    # Identifiers
    IDENTIFIER = auto()

    # Keywords
    PRINT = auto()
    IF = auto()
    ELSE = auto()

    WHILE = auto()
    FOR = auto()
    IN = auto()

    BREAK = auto()
    CONTINUE = auto()

    FN = auto()
    RETURN = auto()

    # Datatypes
    TYPE = auto()

    # Operators
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    MODULO = auto()

    EQUAL_EQUAL = auto()
    NOT_EQUAL = auto()

    LESS = auto()
    GREATER = auto()

    LESS_EQUAL = auto()
    GREATER_EQUAL = auto()

    AND = auto()
    OR = auto()
    NOT = auto()

    RANGE_EXCLUSIVE = auto()
    RANGE_INCLUSIVE = auto()

    # Symbols
    COLON = auto()
    DOUBLE_COLON = auto()
    EQUALS = auto()

    LPAREN = auto()
    RPAREN = auto()

    LBRACKET = auto()
    RBRACKET = auto()

    LBRACE = auto()
    RBRACE = auto()

    DOT = auto()
    QUESTION = auto()
    COMMA = auto()
    
    ARROW = auto()

    # Special
    NEWLINE = auto()
    EOF = auto()

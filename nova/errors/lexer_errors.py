from nova.errors.base import NovaError


class LexerError(NovaError):
    pass


class UnexpectedCharacterError(LexerError):
    pass


class UnterminatedStringError(LexerError):
    pass


class UnterminatedCommentError(LexerError):
    pass


class InvalidFloatLiteralError(LexerError):
    pass
from nova.errors.base import NovaError


class ParserError(NovaError):
    pass


class UnexpectedTokenError(ParserError):
    pass


class UnexpectedEOFError(ParserError):
    pass


class InvalidTypeError(ParserError):
    pass
from nova.errors.runtime_errors import RuntimeError


class TypeError(RuntimeError):
    pass


class DatatypeMismatchError(TypeError):
    pass


class InvalidOperandError(TypeError):
    pass


class InvalidArrayIndexError(TypeError):
    pass


class InvalidArrayAssignmentError(TypeError):
    pass


class InvalidArrayAccessError(TypeError):
    pass
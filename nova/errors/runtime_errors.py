from nova.errors.base import NovaError


class RuntimeError(NovaError):
    pass


class UndeclaredVariableError(RuntimeError):
    pass


class UninitializedVariableError(RuntimeError):
    pass


class DuplicateDeclarationError(RuntimeError):
    pass


class ConstantReassignmentError(RuntimeError):
    pass


class UnknownOperatorError(RuntimeError):
    pass


class NullOperationError(RuntimeError):
    pass
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


class ConditionTypeError(RuntimeError):
    pass


class InvalidRangeError(RuntimeError):
    pass


class NotIterableError(RuntimeError):
    pass


class InvalidLoopControlError(RuntimeError):
    pass

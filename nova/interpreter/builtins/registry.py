from nova.interpreter.builtins.arrays import (
    builtin_length,
    builtin_push,
    builtin_pop,
    builtin_insert,
    builtin_remove,
    builtin_contains,
    builtin_clear,
)

from nova.interpreter.builtins.strings import (
    builtin_upper,
    builtin_lower,
    builtin_trim,
    builtin_starts_with,
    builtin_ends_with,
    builtin_replace,
    builtin_split,
)

from nova.interpreter.builtins.conversion import (
    builtin_to_boolean,
    builtin_to_number,
    builtin_to_string,
)

from nova.interpreter.builtins.maths import (
    builtin_abs,
    builtin_ceil,
    builtin_floor,
    builtin_max,
    builtin_min,
    builtin_pow,
    builtin_random,
    builtin_round,
    builtin_sqrt,
)

from nova.interpreter.builtins.input import builtin_input

BUILTINS = {
    # Arrays
    "length": builtin_length,
    "push": builtin_push,
    "pop": builtin_pop,
    "insert": builtin_insert,
    "remove": builtin_remove,
    "contains": builtin_contains,
    "clear": builtin_clear,
    # Strings
    "upper": builtin_upper,
    "lower": builtin_lower,
    "trim": builtin_trim,
    "startsWith": builtin_starts_with,
    "endsWith": builtin_ends_with,
    "replace": builtin_replace,
    "split": builtin_split,
    # Conversion
    "toBoolean": builtin_to_boolean,
    "toNumber": builtin_to_number,
    "toString": builtin_to_string,
    # Input
    "input": builtin_input,
}

RUNTIME_INTRINSICS = {
    # Maths
    "abs": builtin_abs,
    "min": builtin_min,
    "max": builtin_max,
    "pow": builtin_pow,
    "sqrt": builtin_sqrt,
    "round": builtin_round,
    "floor": builtin_floor,
    "ceil": builtin_ceil,
    "random": builtin_random,
}

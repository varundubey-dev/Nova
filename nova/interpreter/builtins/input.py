from nova.interpreter.runtime_values import (
    StringValue,
)

from nova.errors import (
    FunctionArgumentCountError,
    FunctionArgumentTypeError,
    RuntimeError,
)


def builtin_input(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) > 1:
        raise FunctionArgumentCountError(
            f"Function 'input' expects at most 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    prompt = ""

    if len(arguments) == 1:
        prompt = arguments[0]

        if not isinstance(prompt, StringValue):
            raise FunctionArgumentTypeError(
                "Function 'input' expects a string prompt.",
                node.line,
                node.column,
            )

        prompt = prompt.value

    if interpreter.input_provider is None:
        raise RuntimeError(
            "input() is not supported in the web playground. Use the NOVA CLI for interactive programs.",
            node.line,
            node.column,
        )

    text = interpreter.input_provider(prompt)

    return StringValue(text)
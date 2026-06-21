from nova.interpreter.runtime_values import (
    NumberValue,
    StringValue,
    BooleanValue,
    NullValue,
    ArrayValue,
)

from nova.ast import ArrayType

from nova.errors import (
    DatatypeMismatchError,
    DuplicateDeclarationError,
    UndeclaredVariableError,
    UninitializedVariableError,
    ConstantReassignmentError,
)


class Environment:
    def __init__(self):
        self.variables = {}

    def validate_type(
        self,
        expected_type,
        value,
        line=None,
        column=None,
    ):
        if value is None:
            return

        if isinstance(value, NullValue):
            return

        # Primitive Any
        if expected_type == "U":
            return

        # Primitive Types
        if expected_type == "N":
            if not isinstance(value, NumberValue):
                raise DatatypeMismatchError(
                    "Datatype mismatch.",
                    line,
                    column,
                )
            return

        if expected_type == "S":
            if not isinstance(value, StringValue):
                raise DatatypeMismatchError(
                    "Datatype mismatch.",
                    line,
                    column,
                )
            return

        if expected_type == "B":
            if not isinstance(value, BooleanValue):
                raise DatatypeMismatchError(
                    "Datatype mismatch.",
                    line,
                    column,
                )
            return

        # Array Types
        if isinstance(expected_type, ArrayType):
            if not isinstance(value, ArrayValue):
                raise DatatypeMismatchError(
                    "Datatype mismatch.",
                    line,
                    column,
                )

            allowed_types = expected_type.element_types

            for element in value.value:
                valid = False

                for allowed_type in allowed_types:
                    try:
                        self.validate_type(
                            allowed_type,
                            element,
                            line,
                            column,
                        )
                        valid = True
                        break

                    except Exception:
                        pass

                if not valid:
                    raise DatatypeMismatchError(
                        "Invalid datatype inside array.",
                        line,
                        column,
                    )

            return

        raise DatatypeMismatchError(
            f"Unknown datatype '{expected_type}'.",
            line,
            column,
        )

    def declare_variable(
        self,
        name,
        var_type,
        value=None,
        line=None,
        column=None,
    ):
        if name in self.variables:
            raise DuplicateDeclarationError(
                f"Variable '{name}' already declared.",
                line,
                column,
            )

        self.validate_type(
            var_type,
            value,
            line,
            column,
        )

        self.variables[name] = {
            "type": var_type,
            "value": value,
            "initialized": value is not None,
            "constant": False,
        }

    def declare_constant(
        self,
        name,
        const_type,
        value=None,
        line=None,
        column=None,
    ):
        if name in self.variables:
            raise DuplicateDeclarationError(
                f"Variable '{name}' already declared.",
                line,
                column,
            )

        self.validate_type(
            const_type,
            value,
            line,
            column,
        )

        self.variables[name] = {
            "type": const_type,
            "value": value,
            "initialized": value is not None,
            "constant": True,
        }

    def assign_variable(
        self,
        name,
        value,
        line=None,
        column=None,
    ):
        if name not in self.variables:
            raise UndeclaredVariableError(
                f"Variable '{name}' is not declared.",
                line,
                column,
            )

        variable = self.variables[name]

        if variable["constant"] and variable["initialized"]:
            raise ConstantReassignmentError(
                "Cannot reassign immutable variable.",
                line,
                column,
            )

        self.validate_type(
            variable["type"],
            value,
            line,
            column,
        )

        variable["value"] = value
        variable["initialized"] = True

    def get_variable_info(
        self,
        name,
        line=None,
        column=None,
    ):
        if name not in self.variables:
            raise UndeclaredVariableError(
                f"Variable '{name}' is not declared.",
                line,
                column,
            )

        return self.variables[name]

    def get_variable(
        self,
        name,
        line=None,
        column=None,
    ):
        if name not in self.variables:
            raise UndeclaredVariableError(
                f"Variable '{name}' is not declared.",
                line,
                column,
            )

        variable = self.variables[name]

        if not variable["initialized"]:
            raise UninitializedVariableError(
                f"Variable '{name}' accessed before initialization.",
                line,
                column,
            )

        return variable["value"]

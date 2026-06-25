from nova.interpreter.runtime_values import (
    NumberValue,
    StringValue,
    BooleanValue,
    NullValue,
    ArrayValue,
    MapValue,
)

from nova.ast import ArrayType

from nova.errors import (
    DatatypeMismatchError,
    DuplicateDeclarationError,
    UndeclaredVariableError,
    UninitializedVariableError,
    ConstantReassignmentError,
    UndeclaredFunctionError,
)


class Environment:
    def __init__(self, parent=None):
        self.parent = parent

        self.variables = {}
        self.schemas = {}
        self.functions = {}

    def resolve_variable(
        self,
        name,
        line=None,
        column=None,
    ):
        if name in self.variables:
            return self

        if self.parent is not None:
            return self.parent.resolve_variable(
                name,
                line,
                column,
            )

        raise UndeclaredVariableError(
            f"Variable '{name}' is not declared.",
            line,
            column,
        )

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

                    except DatatypeMismatchError:
                        pass

                if not valid:
                    raise DatatypeMismatchError(
                        "Invalid datatype inside array.",
                        line,
                        column,
                    )

            return

        # Schema Types

        if isinstance(expected_type, str):
            primitive_types = {
                "N",
                "S",
                "B",
                "U",
            }

            if expected_type not in primitive_types:
                schema = self.get_schema(
                    expected_type,
                    line,
                    column,
                )

                self.validate_schema_instance(
                    schema,
                    value,
                    line,
                    column,
                )

                return

        raise DatatypeMismatchError(
            f"Unknown datatype '{expected_type}'.",
            line,
            column,
        )

    def get_schema(
        self,
        name,
        line=None,
        column=None,
    ):
        if name in self.schemas:
            return self.schemas[name]

        if self.parent is not None:
            return self.parent.get_schema(
                name,
                line,
                column,
            )

        raise DatatypeMismatchError(
            f"Unknown schema '{name}'.",
            line,
            column,
        )

    def validate_schema_instance(
        self,
        schema,
        value,
        line=None,
        column=None,
    ):
        if not isinstance(value, MapValue):
            raise DatatypeMismatchError(
                "Datatype mismatch.",
                line,
                column,
            )

        field_lookup = {field.name: field for field in schema.fields}

        # Required fields

        for field in schema.fields:
            if not field.optional and field.name not in value.value:
                raise DatatypeMismatchError(
                    f"Missing required property '{field.name}'.",
                    line,
                    column,
                )

        # Unknown fields

        for key in value.value:
            if key not in field_lookup:
                raise DatatypeMismatchError(
                    f"Unknown property '{key}'.",
                    line,
                    column,
                )

        # Datatype validation

        for key, runtime_value in value.value.items():
            field = field_lookup[key]

            self.validate_type(
                field.field_type,
                runtime_value,
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
        if name in self.variables or name in self.schemas or name in self.functions:
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

    def declare_function(
        self,
        name,
        function,
        line=None,
        column=None,
    ):
        if name in self.variables or name in self.schemas or name in self.functions:
            raise DuplicateDeclarationError(
                f"Function '{name}' already declared.",
                line,
                column,
            )

        self.functions[name] = function

    def declare_schema(
        self,
        name,
        schema,
        line=None,
        column=None,
    ):
        if name in self.schemas or name in self.variables or name in self.functions:
            raise DuplicateDeclarationError(
                f"Schema '{name}' already declared.",
                line,
                column,
            )

        self.schemas[name] = schema

    def declare_constant(
        self,
        name,
        const_type,
        value=None,
        line=None,
        column=None,
    ):
        if name in self.variables or name in self.schemas or name in self.functions:
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
        environment = self.resolve_variable(
            name,
            line,
            column,
        )

        variable = environment.variables[name]

        if variable["constant"] and variable["initialized"]:
            raise ConstantReassignmentError(
                "Cannot reassign immutable variable.",
                line,
                column,
            )

        environment.validate_type(
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
        environment = self.resolve_variable(
            name,
            line,
            column,
        )

        return environment.variables[name]

    def get_variable(
        self,
        name,
        line=None,
        column=None,
    ):
        environment = self.resolve_variable(
            name,
            line,
            column,
        )

        variable = environment.variables[name]

        if not variable["initialized"]:
            raise UninitializedVariableError(
                f"Variable '{name}' accessed before initialization.",
                line,
                column,
            )

        return variable["value"]

    def create_child(self):
        return Environment(parent=self)

    def get_function(
        self,
        name,
        line=None,
        column=None,
    ):
        env = self
        visited = set()

        while env is not None:
            if id(env) in visited:
                raise RuntimeError("Environment cycle detected.")

            visited.add(id(env))

            if name in env.functions:
                return env.functions[name]

            env = env.parent

        raise UndeclaredFunctionError(
            f"Function '{name}' is not declared.",
            line,
            column,
        )
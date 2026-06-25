from nova.interpreter.statements import StatementInterpreter
from nova.interpreter.loop_signals import ReturnSignal

from nova.interpreter.runtime_values import (
    NumberValue,
    StringValue,
    BooleanValue,
    NullValue,
    ArrayValue,
    MapValue,
)

from nova.errors import (
    InvalidOperandError,
    UnknownOperatorError,
    NullOperationError,
    ConditionTypeError,
    StackOverflowError,
    FunctionArgumentCountError,
    MissingReturnError,
)


class ExpressionInterpreter(StatementInterpreter):

    # -------------------------
    # Literals
    # -------------------------

    def visit_number_literal(self, node):
        return NumberValue(node.value)

    def visit_string_literal(self, node):
        return StringValue(node.value)

    def visit_boolean_literal(self, node):
        return BooleanValue(node.value)

    def visit_null_literal(self, node):
        return NullValue()

    def visit_identifier(self, node):
        return self.environment.get_variable(
            node.name,
            node.line,
            node.column,
        )

    def visit_function_call(self, node):
        self.enter_function()

        try:
            if self.call_depth > self.max_call_depth:
                raise StackOverflowError(
                    "Maximum function call depth exceeded.",
                    node.line,
                    node.column,
                )

            function = self.environment.get_function(
                node.callee.name,
                node.line,
                node.column,
            )

            arguments = [self.visit(argument) for argument in node.arguments]

            if len(arguments) != len(function.parameters):
                raise FunctionArgumentCountError(
                    f"Function '{function.name}' expects "
                    f"{len(function.parameters)} argument(s), "
                    f"got {len(arguments)}.",
                    node.line,
                    node.column,
                )

            previous_environment = self.environment
            self.environment = previous_environment.create_child()

            try:
                for parameter, argument in zip(
                    function.parameters,
                    arguments,
                ):
                    self.environment.declare_variable(
                        parameter.name,
                        parameter.parameter_type,
                        argument,
                        node.line,
                        node.column,
                    )

                try:
                    self.visit(function.body)

                except ReturnSignal as signal:
                    if function.return_type is not None:
                        previous_environment.validate_type(
                            function.return_type,
                            signal.value,
                            node.line,
                            node.column,
                        )

                    return signal.value

                # Function finished without executing a return statement.
                if function.return_type is not None:
                    raise MissingReturnError(
                        f"Function '{function.name}' must return a value.",
                        node.line,
                        node.column,
                    )

                return None

            finally:
                self.environment = previous_environment

        finally:
            self.exit_function()

    # -------------------------
    # Condition Validation
    # -------------------------

    def require_boolean_condition(
        self,
        value,
        line,
        column,
    ):
        if not isinstance(
            value,
            BooleanValue,
        ):
            raise ConditionTypeError(
                "Condition must evaluate to a Boolean value.",
                line,
                column,
            )

    # -------------------------
    # Unary Expressions
    # -------------------------

    def visit_unary_expression(self, node):
        operand = self.visit(node.operand)

        if node.operator == "!":
            if not isinstance(
                operand,
                BooleanValue,
            ):
                raise InvalidOperandError(
                    "Operand must be boolean.",
                    node.line,
                    node.column,
                )

            return BooleanValue(not operand.value)

        if node.operator == "-":
            if not isinstance(
                operand,
                NumberValue,
            ):
                raise InvalidOperandError(
                    "Operand must be numeric.",
                    node.line,
                    node.column,
                )

            return NumberValue(-operand.value)

        raise UnknownOperatorError(
            f"Unknown operator '{node.operator}'",
            node.line,
            node.column,
        )

    # -------------------------
    # Binary Expressions
    # -------------------------

    def visit_binary_expression(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        # ---------------------
        # Null Protection
        # ---------------------

        if isinstance(left, NullValue) or isinstance(
            right,
            NullValue,
        ):
            if node.operator not in (
                "==",
                "!=",
            ):
                raise NullOperationError(
                    "Cannot perform operations on null.",
                    node.line,
                    node.column,
                )
        # ---------------------
        # Arithmetic
        # ---------------------

        if node.operator in (
            "+",
            "-",
            "*",
            "/",
            "%",
        ):
            if not isinstance(
                left,
                NumberValue,
            ):
                raise InvalidOperandError(
                    "Left operand must be numeric.",
                    node.line,
                    node.column,
                )

            if not isinstance(
                right,
                NumberValue,
            ):
                raise InvalidOperandError(
                    "Right operand must be numeric.",
                    node.line,
                    node.column,
                )

            if node.operator == "+":
                return NumberValue(left.value + right.value)

            if node.operator == "-":
                return NumberValue(left.value - right.value)

            if node.operator == "*":
                return NumberValue(left.value * right.value)

            if node.operator == "/":
                return NumberValue(left.value / right.value)

            if node.operator == "%":
                return NumberValue(left.value % right.value)

        # ---------------------
        # Comparison
        # ---------------------

        if node.operator in (
            "<",
            ">",
            "<=",
            ">=",
        ):
            if not isinstance(
                left,
                NumberValue,
            ):
                raise InvalidOperandError(
                    "Left operand must be numeric.",
                    node.line,
                    node.column,
                )

            if not isinstance(
                right,
                NumberValue,
            ):
                raise InvalidOperandError(
                    "Right operand must be numeric.",
                    node.line,
                    node.column,
                )

            if node.operator == "<":
                return BooleanValue(left.value < right.value)

            if node.operator == ">":
                return BooleanValue(left.value > right.value)

            if node.operator == "<=":
                return BooleanValue(left.value <= right.value)

            if node.operator == ">=":
                return BooleanValue(left.value >= right.value)

        # ---------------------
        # Null Equality
        # ---------------------

        if isinstance(left, NullValue) and isinstance(right, NullValue):
            if node.operator == "==":
                return BooleanValue(True)

            if node.operator == "!=":
                return BooleanValue(False)

        # ---------------------
        # Equality
        # ---------------------

        if node.operator == "==":
            return BooleanValue(type(left) is type(right) and left.value == right.value)

        if node.operator == "!=":
            return BooleanValue(
                not (type(left) is type(right) and left.value == right.value)
            )

        # ---------------------
        # Logical
        # ---------------------

        if node.operator in (
            "&&",
            "||",
        ):
            if not isinstance(
                left,
                BooleanValue,
            ):
                raise InvalidOperandError(
                    "Left operand must be boolean.",
                    node.line,
                    node.column,
                )

            if not isinstance(
                right,
                BooleanValue,
            ):
                raise InvalidOperandError(
                    "Right operand must be boolean.",
                    node.line,
                    node.column,
                )

            if node.operator == "&&":
                return BooleanValue(left.value and right.value)

            if node.operator == "||":
                return BooleanValue(left.value or right.value)

        raise UnknownOperatorError(
            f"Unknown operator '{node.operator}'",
            node.line,
            node.column,
        )

    # -------------------------
    # Ternary Expressions
    # -------------------------

    def visit_ternary_expression(self, node):
        condition = self.visit(node.condition)

        self.require_boolean_condition(
            condition,
            node.line,
            node.column,
        )

        if condition.value:
            return self.visit(node.true_expression)

        return self.visit(node.false_expression)

    # -------------------------
    # Output Formatting
    # -------------------------

    def format_value(self, value):
        if isinstance(value, NumberValue):
            return str(value.value)

        if isinstance(value, StringValue):
            return value.value

        if isinstance(value, BooleanValue):
            return "true" if value.value else "false"

        if isinstance(value, NullValue):
            return "null"

        if isinstance(value, ArrayValue):
            elements = [self.format_value(element) for element in value.value]

            return "[" + ", ".join(elements) + "]"

        if isinstance(value, MapValue):
            properties = []

            for key, property_value in value.value.items():
                properties.append(f"{key} = {self.format_value(property_value)}")

            return "{ " + ", ".join(properties) + " }"

        return str(value)

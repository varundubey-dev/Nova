from nova.interpreter.statements import StatementInterpreter

from nova.interpreter.runtime_values import (
    NumberValue,
    StringValue,
    BooleanValue,
    NullValue,
    ArrayValue,
)

from nova.errors import (
    InvalidOperandError,
    UnknownOperatorError,
    NullOperationError,
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

        return str(value)

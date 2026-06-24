from nova.interpreter.base import InterpreterBase
from nova.interpreter.runtime_values import (
    BooleanValue,
    NumberValue,
    ArrayValue,
)

from nova.interpreter.loop_signals import (
    BreakSignal,
    ContinueSignal,
)

from nova.errors import (
    ConditionTypeError,
    InvalidRangeError,
    NotIterableError,
    InvalidLoopControlError,
)


class StatementInterpreter(InterpreterBase):
    def visit_program(self, node):
        result = None

        for statement in node.statements:
            result = self.visit(statement)

        return result

    def visit_variable_declaration(self, node):
        value = None

        if node.value is not None:
            value = self.visit(node.value)

        self.environment.declare_variable(
            node.name,
            node.var_type,
            value,
            node.line,
            node.column,
        )

        return value

    def visit_constant_declaration(self, node):
        value = None

        if node.value is not None:
            value = self.visit(node.value)

        self.environment.declare_constant(
            node.name,
            node.const_type,
            value,
            node.line,
            node.column,
        )

        return value

    def visit_schema_declaration(self, node):
        self.environment.declare_schema(
            node.name,
            node.schema,
            node.line,
            node.column,
        )

        return None

    def visit_assignment(self, node):
        value = self.visit(node.value)

        self.environment.assign_variable(
            node.name,
            value,
            node.line,
            node.column,
        )

        return value

    def visit_print_statement(self, node):
        values = [self.visit(expression) for expression in node.expressions]

        self.output.append(" ".join(self.format_value(value) for value in values))

        return None

    def visit_block_statement(self, node):
        previous_environment = self.environment

        self.environment = self.environment.create_child()

        try:
            result = None

            for statement in node.statements:
                result = self.visit(statement)

            return result

        finally:
            self.environment = previous_environment

    def visit_if_statement(self, node):
        condition = self.visit(node.condition)

        if not isinstance(
            condition,
            BooleanValue,
        ):
            raise ConditionTypeError(
                "Condition must evaluate to a Boolean value.",
                node.line,
                node.column,
            )

        if condition.value:
            return self.visit(node.then_branch)

        if node.else_branch is not None:
            return self.visit(node.else_branch)

        return None

    def visit_while_statement(self, node):
        self.enter_loop()

        try:
            while True:
                condition = self.visit(node.condition)

                if not isinstance(
                    condition,
                    BooleanValue,
                ):
                    raise ConditionTypeError(
                        "Condition must evaluate to a Boolean value.",
                        node.line,
                        node.column,
                    )

                if not condition.value:
                    break

                try:
                    self.visit(node.body)

                except ContinueSignal:
                    continue

                except BreakSignal:
                    break

        finally:
            self.exit_loop()

        return None

    def visit_for_range_statement(self, node):
        start = self.visit(node.start)
        end = self.visit(node.end)

        if not isinstance(start, NumberValue):
            raise InvalidRangeError(
                "Range bounds must be numeric.",
                node.line,
                node.column,
            )

        if not isinstance(end, NumberValue):
            raise InvalidRangeError(
                "Range bounds must be numeric.",
                node.line,
                node.column,
            )

        start_value = int(start.value)
        end_value = int(end.value)

        if start_value <= end_value:
            stop = end_value + 1 if node.inclusive else end_value
            values = range(start_value, stop)

        else:
            stop = end_value - 1 if node.inclusive else end_value
            values = range(start_value, stop, -1)

        self.enter_loop()

        try:
            for value in values:
                previous_environment = self.environment

                self.environment = self.environment.create_child()

                try:
                    self.environment.declare_variable(
                        node.variable_name,
                        "N",
                        NumberValue(value),
                    )

                    try:
                        self.visit(node.body)

                    except ContinueSignal:
                        continue

                    except BreakSignal:
                        break

                finally:
                    self.environment = previous_environment

        finally:
            self.exit_loop()

        return None

    def visit_for_each_statement(self, node):
        iterable = self.visit(node.iterable)

        if not isinstance(
            iterable,
            ArrayValue,
        ):
            raise NotIterableError(
                "Value is not iterable.",
                node.line,
                node.column,
            )

        self.enter_loop()

        try:
            for element in iterable.value:
                previous_environment = self.environment

                self.environment = self.environment.create_child()

                try:
                    self.environment.declare_variable(
                        node.variable_name,
                        "U",
                        element,
                    )

                    try:
                        self.visit(node.body)

                    except ContinueSignal:
                        continue

                    except BreakSignal:
                        break

                finally:
                    self.environment = previous_environment

        finally:
            self.exit_loop()

        return None

    def visit_break_statement(self, node):
        if self.loop_depth == 0:
            raise InvalidLoopControlError(
                "Break statement can only be used inside a loop.",
                node.line,
                node.column,
            )

        raise BreakSignal()

    def visit_continue_statement(self, node):
        if self.loop_depth == 0:
            raise InvalidLoopControlError(
                "Continue statement can only be used inside a loop.",
                node.line,
                node.column,
            )

        raise ContinueSignal()

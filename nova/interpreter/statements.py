from nova.interpreter.base import InterpreterBase


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
        value = self.visit(node.expression)

        self.output.append(self.format_value(value))

        return value

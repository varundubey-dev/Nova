from nova.interpreter.environment import Environment

from nova.ast import (
    Program,
    VariableDeclaration,
    ConstantDeclaration,
    Assignment,
    PrintStatement,
    Identifier,
    NumberLiteral,
    StringLiteral,
    BooleanLiteral,
    NullLiteral,
    ArrayLiteral,
    ArrayAccess,
    ArrayAssignment,
    BinaryExpression,
    UnaryExpression,
)


class InterpreterBase:
    def __init__(self):
        self.environment = Environment()

    def interpret(self, program):
        return self.visit(program)

    def visit(self, node):
        if isinstance(node, Program):
            return self.visit_program(node)

        if isinstance(node, VariableDeclaration):
            return self.visit_variable_declaration(node)

        if isinstance(node, ConstantDeclaration):
            return self.visit_constant_declaration(node)

        if isinstance(node, Assignment):
            return self.visit_assignment(node)

        if isinstance(node, PrintStatement):
            return self.visit_print_statement(node)

        if isinstance(node, NumberLiteral):
            return self.visit_number_literal(node)

        if isinstance(node, StringLiteral):
            return self.visit_string_literal(node)

        if isinstance(node, BooleanLiteral):
            return self.visit_boolean_literal(node)

        if isinstance(node, NullLiteral):
            return self.visit_null_literal(node)

        if isinstance(node, ArrayLiteral):
            return self.visit_array_literal(node)

        if isinstance(node, ArrayAccess):
            return self.visit_array_access(node)

        if isinstance(node, ArrayAssignment):
            return self.visit_array_assignment(node)

        if isinstance(node, Identifier):
            return self.visit_identifier(node)

        if isinstance(node, UnaryExpression):
            return self.visit_unary_expression(node)

        if isinstance(node, BinaryExpression):
            return self.visit_binary_expression(node)

        raise NotImplementedError(
            f"Unknown node type: {type(node).__name__}"
        )

    # -------------------------
    # Statement Visitors
    # -------------------------

    def visit_program(self, node):
        raise NotImplementedError

    def visit_variable_declaration(self, node):
        raise NotImplementedError

    def visit_constant_declaration(self, node):
        raise NotImplementedError

    def visit_assignment(self, node):
        raise NotImplementedError

    def visit_print_statement(self, node):
        raise NotImplementedError

    # -------------------------
    # Literal Visitors
    # -------------------------

    def visit_number_literal(self, node):
        raise NotImplementedError

    def visit_string_literal(self, node):
        raise NotImplementedError

    def visit_boolean_literal(self, node):
        raise NotImplementedError

    def visit_null_literal(self, node):
        raise NotImplementedError

    def visit_identifier(self, node):
        raise NotImplementedError

    # -------------------------
    # Expressions
    # -------------------------

    def visit_unary_expression(self, node):
        raise NotImplementedError

    def visit_binary_expression(self, node):
        raise NotImplementedError

    # -------------------------
    # Arrays
    # -------------------------

    def visit_array_literal(self, node):
        raise NotImplementedError

    def visit_array_access(self, node):
        raise NotImplementedError

    def visit_array_assignment(self, node):
        raise NotImplementedError

    # -------------------------
    # Helpers
    # -------------------------

    def format_value(self, value):
        raise NotImplementedError

    def get_array_root(self, target):
        raise NotImplementedError

    def get_element_type(self, array_type, depth):
        raise NotImplementedError

    def get_array_depth(self, target):
        raise NotImplementedError
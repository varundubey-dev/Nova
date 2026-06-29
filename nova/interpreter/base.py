from nova.interpreter.environment import Environment
from nova.errors import RuntimeError
import time
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
    TernaryExpression,
    IfStatement,
    BlockStatement,
    WhileStatement,
    ForRangeStatement,
    ForEachStatement,
    SchemaDeclaration,
    MapLiteral,
    PropertyAccess,
    PropertyAssignment,
    BreakStatement,
    ContinueStatement,
    FunctionDeclaration,
    FunctionCall,
    ReturnStatement,
    ImportStatement,
)


class InterpreterBase:
    def __init__(
        self,
        input_provider=None,
        resolver=None,
        is_stdlib=False,
        output_callback=None,
    ):
        self.environment = Environment()

        self.output = []

        self.output_callback = output_callback

        self.input_provider = input_provider

        self.resolver = resolver

        self.is_stdlib = is_stdlib

        self.loop_depth = 0

        self.call_depth = 0
        self.max_call_depth = 500
        self.execution_steps = 0
        self.max_execution_steps = 1_000_000
        self.start_time = time.monotonic()
        self.max_execution_time = 2.0

        self.max_output_lines = 1000

    def interpret(self, program):
        return self.visit(program)

    def visit(self, node):
        try:
            self.check_limits(node)
        
            self.check_limits(node)
            if isinstance(node, Program):
                return self.visit_program(node)

            if isinstance(node, VariableDeclaration):
                return self.visit_variable_declaration(node)

            if isinstance(node, ConstantDeclaration):
                return self.visit_constant_declaration(node)

            if isinstance(node, Assignment):
                return self.visit_assignment(node)

            if isinstance(node, SchemaDeclaration):
                return self.visit_schema_declaration(node)

            if isinstance(node, PropertyAssignment):
                return self.visit_property_assignment(node)

            if isinstance(node, ImportStatement):
                return self.visit_import_statement(node)

            if isinstance(node, PrintStatement):
                return self.visit_print_statement(node)

            if isinstance(node, BlockStatement):
                return self.visit_block_statement(node)

            if isinstance(node, IfStatement):
                return self.visit_if_statement(node)

            if isinstance(node, WhileStatement):
                return self.visit_while_statement(node)

            if isinstance(node, ForRangeStatement):
                return self.visit_for_range_statement(node)

            if isinstance(node, ForEachStatement):
                return self.visit_for_each_statement(node)

            if isinstance(node, BreakStatement):
                return self.visit_break_statement(node)

            if isinstance(node, ContinueStatement):
                return self.visit_continue_statement(node)

            if isinstance(node, FunctionDeclaration):
                return self.visit_function_declaration(node)

            if isinstance(node, ReturnStatement):
                return self.visit_return_statement(node)

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

            if isinstance(node, MapLiteral):
                return self.visit_map_literal(node)

            if isinstance(node, PropertyAccess):
                return self.visit_property_access(node)

            if isinstance(node, Identifier):
                return self.visit_identifier(node)

            if isinstance(node, FunctionCall):
                return self.visit_function_call(node)

            if isinstance(node, UnaryExpression):
                return self.visit_unary_expression(node)

            if isinstance(node, BinaryExpression):
                return self.visit_binary_expression(node)

            if isinstance(node, TernaryExpression):
                return self.visit_ternary_expression(node)

            raise NotImplementedError(f"Unknown node type: {type(node).__name__}")
        
        except RecursionError:
            raise RuntimeError(
                "Maximum recursion depth exceeded.",
                node.line,
                node.column,
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

    def visit_schema_declaration(self, node):
        raise NotImplementedError

    def visit_function_declaration(self, node):
        raise NotImplementedError

    def visit_return_statement(self, node):
        raise NotImplementedError

    def visit_property_assignment(self, node):
        raise NotImplementedError

    def visit_import_statement(self, node):
        raise NotImplementedError

    def visit_print_statement(self, node):
        raise NotImplementedError

    def visit_block_statement(self, node):
        raise NotImplementedError

    def visit_if_statement(self, node):
        raise NotImplementedError

    def visit_while_statement(self, node):
        raise NotImplementedError

    def visit_for_range_statement(self, node):
        raise NotImplementedError

    def visit_for_each_statement(self, node):
        raise NotImplementedError

    def visit_break_statement(self, node):
        raise NotImplementedError

    def visit_continue_statement(self, node):
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

    def visit_function_call(self, node):
        raise NotImplementedError

    # -------------------------
    # Expressions
    # -------------------------

    def visit_unary_expression(self, node):
        raise NotImplementedError

    def visit_binary_expression(self, node):
        raise NotImplementedError

    def visit_map_literal(self, node):
        raise NotImplementedError

    def visit_property_access(self, node):
        raise NotImplementedError

    def visit_ternary_expression(self, node):
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

    def enter_loop(self):
        self.loop_depth += 1

    def exit_loop(self):
        self.loop_depth -= 1

    def enter_function(self, node):
        self.call_depth += 1

        if self.call_depth > self.max_call_depth:
            raise RuntimeError(
                "Maximum recursion depth exceeded.",
                node.line,
                node.column,
            )

    def exit_function(self):
        self.call_depth -= 1
    
    def check_limits(self, node):
        self.execution_steps += 1

        if self.execution_steps > self.max_execution_steps:
            raise RuntimeError(
                "Execution limit exceeded.",
                node.line,
                node.column,
            )

        if time.monotonic() - self.start_time > self.max_execution_time:
            raise RuntimeError(
                "Execution timed out.",
                node.line,
                node.column,
            )

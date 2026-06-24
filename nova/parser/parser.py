from nova.lexer.token_types import TokenType

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
    ArrayType,
    ArrayLiteral,
    ArrayAccess,
    ArrayAssignment,
    BinaryExpression,
    UnaryExpression,
    SchemaDeclaration,
    SchemaType,
    SchemaField,
    MapLiteral,
    MapEntry,
    PropertyAccess,
    PropertyAssignment,
    IfStatement,
    BlockStatement,
    TernaryExpression,
    WhileStatement,
    ForRangeStatement,
    ForEachStatement,
    BreakStatement,
    ContinueStatement,
)

from nova.errors import (
    UnexpectedTokenError,
    UnexpectedEOFError,
    InvalidTypeError,
)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

        self.position = 0

        self.current_token = tokens[0] if tokens else None

        self.paren_depth = 0

    def advance(self):
        self.position += 1

        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def peek(self):
        next_position = self.position + 1

        if next_position >= len(self.tokens):
            return None

        return self.tokens[next_position]

    def consume(self, expected_type):
        if self.current_token is None:
            last_token = self.tokens[self.position - 1]

            raise UnexpectedEOFError(
                f"Expected {expected_type.name}, got EOF.",
                last_token.line,
                last_token.column,
            )

        if self.current_token.type != expected_type:
            raise UnexpectedTokenError(
                f"Expected {expected_type.name}, got {self.current_token.type.name}.",
                self.current_token.line,
                self.current_token.column,
            )

        token = self.current_token

        self.advance()

        return token

    def parse(self):
        statements = []

        while (
            self.current_token is not None and self.current_token.type != TokenType.EOF
        ):
            if self.current_token.type == TokenType.NEWLINE:
                self.advance()
                continue

            statements.append(self.parse_statement())

        return Program(statements)

    def parse_statement(self):
        if self.current_token is None:
            last_token = self.tokens[self.position - 1]

            raise UnexpectedEOFError(
                "Unexpected EOF while parsing statement.",
                last_token.line,
                last_token.column,
            )

        if self.current_token.type == TokenType.PRINT:
            return self.parse_print_statement()

        if self.current_token.type == TokenType.IF:
            return self.parse_if_statement()

        if self.current_token.type == TokenType.WHILE:
            return self.parse_while_statement()

        if self.current_token.type == TokenType.FOR:
            return self.parse_for_statement()

        if self.current_token.type == TokenType.BREAK:
            return self.parse_break_statement()

        if self.current_token.type == TokenType.CONTINUE:
            return self.parse_continue_statement()

        if self.current_token.type == TokenType.IDENTIFIER:
            next_token = self.peek()

            if next_token is None:
                raise UnexpectedEOFError(
                    "Unexpected EOF while parsing statement.",
                    self.current_token.line,
                    self.current_token.column,
                )

            if next_token.type == TokenType.COLON:
                if self.is_schema_declaration():
                    return self.parse_schema_declaration()

                return self.parse_variable_declaration()

            if next_token.type == TokenType.DOUBLE_COLON:
                return self.parse_constant_declaration()

            if self.is_array_assignment():
                return self.parse_array_assignment()

            if self.is_property_assignment():
                return self.parse_property_assignment()

            if next_token.type == TokenType.EQUALS:
                return self.parse_assignment()

        raise UnexpectedTokenError(
            f"Unexpected token {self.current_token.type.name}.",
            self.current_token.line,
            self.current_token.column,
        )

    def parse_variable_declaration(self):
        name_token = self.consume(TokenType.IDENTIFIER)

        self.consume(TokenType.COLON)

        var_type = self.parse_type()

        value = None

        if (
            self.current_token is not None
            and self.current_token.type == TokenType.EQUALS
        ):
            self.advance()

            value = self.parse_expression()

        return VariableDeclaration(
            name=name_token.value,
            var_type=var_type,
            value=value,
            line=name_token.line,
            column=name_token.column,
        )

    def parse_constant_declaration(self):
        name_token = self.consume(TokenType.IDENTIFIER)

        self.consume(TokenType.DOUBLE_COLON)

        const_type = self.parse_type()

        value = None

        if (
            self.current_token is not None
            and self.current_token.type == TokenType.EQUALS
        ):
            self.advance()

            value = self.parse_expression()

        return ConstantDeclaration(
            name=name_token.value,
            const_type=const_type,
            value=value,
            line=name_token.line,
            column=name_token.column,
        )

    def parse_type(self):
        if self.current_token is None:
            last_token = self.tokens[self.position - 1]

            raise UnexpectedEOFError(
                "Unexpected EOF while parsing type.",
                last_token.line,
                last_token.column,
            )

        # Built-in types
        if self.current_token.type == TokenType.TYPE:
            token = self.current_token

            self.advance()

            return token.value

        # User-defined schema types
        if self.current_token.type == TokenType.IDENTIFIER:
            token = self.current_token

            self.advance()

            return token.value

        # Array types
        if self.current_token.type == TokenType.LBRACKET:
            return self.parse_array_type()

        raise InvalidTypeError(
            "Expected type.",
            self.current_token.line,
            self.current_token.column,
        )

    def parse_array_type(self):
        self.consume(TokenType.LBRACKET)

        element_types = []

        while True:
            element_types.append(self.parse_type())

            if (
                self.current_token is not None
                and self.current_token.type == TokenType.COMMA
            ):
                self.advance()
                continue

            break

        self.consume(TokenType.RBRACKET)

        return ArrayType(element_types)

    def parse_array_literal(self):
        lbracket = self.consume(TokenType.LBRACKET)

        elements = []

        self.skip_newlines()

        # Empty array: []
        if (
            self.current_token is not None
            and self.current_token.type == TokenType.RBRACKET
        ):
            self.advance()

            return ArrayLiteral(
                elements,
                line=lbracket.line,
                column=lbracket.column,
            )

        while True:
            self.skip_newlines()

            elements.append(self.parse_expression())

            self.skip_newlines()

            if (
                self.current_token is not None
                and self.current_token.type == TokenType.COMMA
            ):
                self.advance()

                self.skip_newlines()

                continue

            break

        self.consume(TokenType.RBRACKET)

        return ArrayLiteral(
            elements,
            line=lbracket.line,
            column=lbracket.column,
        )

    def skip_newlines(self):
        while (
            self.current_token is not None
            and self.current_token.type == TokenType.NEWLINE
        ):
            self.advance()

    def skip_expression_newlines(self):
        if self.paren_depth > 0:
            self.skip_newlines()

    def parse_postfix_expression(self, expression):
        while self.current_token is not None:

            # Array access
            if self.current_token.type == TokenType.LBRACKET:
                self.advance()

                index = self.parse_expression()

                self.consume(TokenType.RBRACKET)

                expression = ArrayAccess(
                    array=expression,
                    index=index,
                    line=expression.line,
                    column=expression.column,
                )

                continue

            # Property access
            if self.current_token.type == TokenType.DOT:
                self.advance()

                property_token = self.consume(TokenType.IDENTIFIER)

                expression = PropertyAccess(
                    target=expression,
                    property_name=property_token.value,
                    line=expression.line,
                    column=expression.column,
                )

                continue

            break

        return expression

    def is_array_assignment(self):
        pos = self.position

        seen_bracket = False
        last_meaningful = None

        while pos < len(self.tokens):
            token = self.tokens[pos]

            if token.type == TokenType.LBRACKET:
                seen_bracket = True

            elif token.type == TokenType.EQUALS:
                return seen_bracket and last_meaningful == TokenType.RBRACKET

            elif token.type not in (TokenType.NEWLINE,):
                last_meaningful = token.type

            if token.type == TokenType.EOF:
                return False

            pos += 1

        return False

    def parse_array_assignment(self):
        name_token = self.consume(TokenType.IDENTIFIER)

        target = Identifier(
            name_token.value,
            line=name_token.line,
            column=name_token.column,
        )

        target = self.parse_postfix_expression(target)

        self.consume(TokenType.EQUALS)

        value = self.parse_expression()

        return ArrayAssignment(
            target=target,
            value=value,
            line=target.line,
            column=target.column,
        )

    def parse_assignment(self):
        name_token = self.consume(TokenType.IDENTIFIER)

        self.consume(TokenType.EQUALS)

        value = self.parse_expression()

        return Assignment(
            name=name_token.value,
            value=value,
            line=name_token.line,
            column=name_token.column,
        )

    def parse_print_statement(self):
        print_token = self.consume(TokenType.PRINT)

        self.consume(TokenType.LPAREN)

        self.paren_depth += 1

        try:
            self.skip_newlines()

            expressions = [self.parse_expression()]

            while (
                self.current_token is not None
                and self.current_token.type == TokenType.COMMA
            ):
                self.advance()

                self.skip_newlines()

                expressions.append(self.parse_expression())

            self.skip_newlines()

            self.consume(TokenType.RPAREN)

        finally:
            self.paren_depth -= 1

        return PrintStatement(
            expressions,
            line=print_token.line,
            column=print_token.column,
        )

    def parse_expression(self):
        self.skip_expression_newlines()
        return self.parse_ternary()

    def parse_ternary(self):
        condition = self.parse_or()

        self.skip_expression_newlines()

        if (
            self.current_token is not None
            and self.current_token.type == TokenType.QUESTION
        ):
            token = self.current_token

            self.advance()

            self.skip_expression_newlines()

            true_expression = self.parse_expression()

            self.skip_expression_newlines()

            self.consume(TokenType.COLON)

            self.skip_expression_newlines()

            false_expression = self.parse_expression()

            return TernaryExpression(
                condition=condition,
                true_expression=true_expression,
                false_expression=false_expression,
                line=token.line,
                column=token.column,
            )

        return condition

    def parse_or(self):
        left = self.parse_and()

        while True:
            self.skip_expression_newlines()

            if self.current_token is None or self.current_token.type != TokenType.OR:
                break

            token = self.current_token
            operator = token.value

            self.advance()

            self.skip_expression_newlines()

            right = self.parse_and()

            left = BinaryExpression(
                left,
                operator,
                right,
                line=token.line,
                column=token.column,
            )

        return left

    def parse_and(self):
        left = self.parse_equality()

        while True:
            self.skip_expression_newlines()

            if self.current_token is None or self.current_token.type != TokenType.AND:
                break

            token = self.current_token
            operator = token.value

            self.advance()

            self.skip_expression_newlines()

            right = self.parse_equality()

            left = BinaryExpression(
                left,
                operator,
                right,
                line=token.line,
                column=token.column,
            )

        return left

    def parse_equality(self):
        left = self.parse_comparison()

        while True:
            self.skip_expression_newlines()

            if self.current_token is None or self.current_token.type not in (
                TokenType.EQUAL_EQUAL,
                TokenType.NOT_EQUAL,
            ):
                break

            token = self.current_token
            operator = token.value

            self.advance()

            self.skip_expression_newlines()

            right = self.parse_comparison()

            left = BinaryExpression(
                left,
                operator,
                right,
                line=token.line,
                column=token.column,
            )

        return left

    def parse_comparison(self):
        left = self.parse_additive()

        while True:
            self.skip_expression_newlines()

            if self.current_token is None or self.current_token.type not in (
                TokenType.LESS,
                TokenType.GREATER,
                TokenType.LESS_EQUAL,
                TokenType.GREATER_EQUAL,
            ):
                break

            token = self.current_token
            operator = token.value

            self.advance()

            self.skip_expression_newlines()

            right = self.parse_additive()

            left = BinaryExpression(
                left,
                operator,
                right,
                line=token.line,
                column=token.column,
            )

        return left

    def parse_additive(self):
        left = self.parse_multiplicative()

        while True:
            self.skip_expression_newlines()

            if self.current_token is None or self.current_token.type not in (
                TokenType.PLUS,
                TokenType.MINUS,
            ):
                break

            token = self.current_token
            operator = token.value

            self.advance()

            self.skip_expression_newlines()

            right = self.parse_multiplicative()

            left = BinaryExpression(
                left,
                operator,
                right,
                line=token.line,
                column=token.column,
            )

        return left

    def parse_multiplicative(self):
        left = self.parse_unary()

        while True:
            self.skip_expression_newlines()

            if self.current_token is None or self.current_token.type not in (
                TokenType.STAR,
                TokenType.SLASH,
                TokenType.MODULO,
            ):
                break

            token = self.current_token
            operator = token.value

            self.advance()

            self.skip_expression_newlines()

            right = self.parse_unary()

            left = BinaryExpression(
                left,
                operator,
                right,
                line=token.line,
                column=token.column,
            )

        return left

    def parse_unary(self):
        self.skip_expression_newlines()

        if self.current_token is not None and self.current_token.type in (
            TokenType.NOT,
            TokenType.MINUS,
        ):
            token = self.current_token
            operator = token.value

            self.advance()

            self.skip_expression_newlines()

            operand = self.parse_unary()

            return UnaryExpression(
                operator,
                operand,
                line=token.line,
                column=token.column,
            )

        return self.parse_primary()

    def parse_primary(self):
        self.skip_expression_newlines()

        if self.current_token is None:
            last_token = self.tokens[self.position - 1]

            raise UnexpectedEOFError(
                "Unexpected EOF while parsing expression.",
                last_token.line,
                last_token.column,
            )

        token = self.current_token

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberLiteral(
                token.value,
                line=token.line,
                column=token.column,
            )

        if token.type == TokenType.STRING:
            self.advance()
            return StringLiteral(
                token.value,
                line=token.line,
                column=token.column,
            )

        if token.type == TokenType.BOOLEAN:
            self.advance()
            return BooleanLiteral(
                token.value,
                line=token.line,
                column=token.column,
            )

        if token.type == TokenType.NULL:
            self.advance()
            return NullLiteral(
                line=token.line,
                column=token.column,
            )

        if token.type == TokenType.LBRACKET:
            return self.parse_array_literal()

        if token.type == TokenType.LBRACE:
            return self.parse_map_literal()

        if token.type == TokenType.IDENTIFIER:
            self.advance()

            expression = Identifier(
                token.value,
                line=token.line,
                column=token.column,
            )

            return self.parse_postfix_expression(expression)

        if token.type == TokenType.LPAREN:
            self.advance()

            expression = self.parse_grouped_expression()

            self.consume(TokenType.RPAREN)

            return expression

        raise UnexpectedTokenError(
            f"Unexpected token {token.type.name}.",
            token.line,
            token.column,
        )

    def is_schema_declaration(self):
        if self.current_token is None:
            return False

        if self.current_token.type != TokenType.IDENTIFIER:
            return False

        pos = self.position + 1

        if pos >= len(self.tokens):
            return False

        if self.tokens[pos].type != TokenType.COLON:
            return False

        pos += 1

        if pos >= len(self.tokens):
            return False

        token = self.tokens[pos]

        return token.type == TokenType.TYPE and token.value == "M"

    def parse_schema_declaration(self):
        name_token = self.consume(TokenType.IDENTIFIER)

        self.consume(TokenType.COLON)

        map_type = self.consume(TokenType.TYPE)

        if map_type.value != "M":
            raise InvalidTypeError(
                "Expected map schema type M.",
                map_type.line,
                map_type.column,
            )

        self.consume(TokenType.EQUALS)

        schema = self.parse_schema_type()

        return SchemaDeclaration(
            name=name_token.value,
            schema=schema,
            line=name_token.line,
            column=name_token.column,
        )

    def parse_schema_type(self):
        lbrace = self.consume(TokenType.LBRACE)

        fields = []

        self.skip_newlines()

        if (
            self.current_token is not None
            and self.current_token.type == TokenType.RBRACE
        ):
            self.advance()

            return SchemaType(
                fields,
                line=lbrace.line,
                column=lbrace.column,
            )

        while True:
            self.skip_newlines()

            field_name = self.consume(TokenType.IDENTIFIER)

            optional = False

            if (
                self.current_token is not None
                and self.current_token.type == TokenType.QUESTION
            ):
                optional = True
                self.advance()

            self.consume(TokenType.COLON)

            field_type = self.parse_type()

            fields.append(
                SchemaField(
                    name=field_name.value,
                    field_type=field_type,
                    optional=optional,
                    line=field_name.line,
                    column=field_name.column,
                )
            )

            self.skip_newlines()

            if (
                self.current_token is not None
                and self.current_token.type == TokenType.COMMA
            ):
                self.advance()
                continue

            break

        self.skip_newlines()

        self.consume(TokenType.RBRACE)

        return SchemaType(
            fields,
            line=lbrace.line,
            column=lbrace.column,
        )

    def parse_map_literal(self):
        lbrace = self.consume(TokenType.LBRACE)

        entries = []

        self.skip_newlines()

        if (
            self.current_token is not None
            and self.current_token.type == TokenType.RBRACE
        ):
            self.advance()

            return MapLiteral(
                entries,
                line=lbrace.line,
                column=lbrace.column,
            )

        while True:
            self.skip_newlines()

            key_token = self.consume(TokenType.IDENTIFIER)

            self.consume(TokenType.EQUALS)

            value = self.parse_expression()

            entries.append(
                MapEntry(
                    key=key_token.value,
                    value=value,
                    line=key_token.line,
                    column=key_token.column,
                )
            )

            self.skip_newlines()

            if (
                self.current_token is not None
                and self.current_token.type == TokenType.COMMA
            ):
                self.advance()
                continue

            break

        self.skip_newlines()

        self.consume(TokenType.RBRACE)

        return MapLiteral(
            entries,
            line=lbrace.line,
            column=lbrace.column,
        )

    def is_property_assignment(self):
        pos = self.position

        seen_property = False
        last_meaningful = None

        while pos < len(self.tokens):
            token = self.tokens[pos]

            if token.type == TokenType.DOT:
                seen_property = True

            elif token.type == TokenType.EQUALS:
                return seen_property and last_meaningful != TokenType.RBRACKET

            elif token.type not in (TokenType.NEWLINE,):
                last_meaningful = token.type

            if token.type == TokenType.EOF:
                return False

            pos += 1

        return False

    def parse_property_assignment(self):
        name_token = self.consume(TokenType.IDENTIFIER)

        target = Identifier(
            name_token.value,
            line=name_token.line,
            column=name_token.column,
        )

        target = self.parse_postfix_expression(target)

        self.consume(TokenType.EQUALS)

        value = self.parse_expression()

        return PropertyAssignment(
            target=target,
            value=value,
            line=target.line,
            column=target.column,
        )

    def parse_block_statement(self):
        lbrace = self.consume(TokenType.LBRACE)

        statements = []

        self.skip_newlines()

        while (
            self.current_token is not None
            and self.current_token.type != TokenType.RBRACE
        ):
            statements.append(self.parse_statement())
            self.skip_newlines()

        self.consume(TokenType.RBRACE)

        return BlockStatement(
            statements,
            line=lbrace.line,
            column=lbrace.column,
        )

    def parse_if_statement(self):
        if_token = self.consume(TokenType.IF)

        condition = self.parse_expression()

        then_branch = self.parse_block_statement()

        else_branch = None

        self.skip_newlines()

        if self.current_token is not None and self.current_token.type == TokenType.ELSE:
            self.advance()

            self.skip_newlines()

            if (
                self.current_token is not None
                and self.current_token.type == TokenType.IF
            ):
                else_branch = self.parse_if_statement()

            else:
                else_branch = self.parse_block_statement()

        return IfStatement(
            condition=condition,
            then_branch=then_branch,
            else_branch=else_branch,
            line=if_token.line,
            column=if_token.column,
        )

    def parse_grouped_expression(self):
        self.paren_depth += 1

        try:
            self.skip_newlines()

            expression = self.parse_expression()

            self.skip_newlines()

            return expression

        finally:
            self.paren_depth -= 1

    def parse_while_statement(self):
        while_token = self.consume(TokenType.WHILE)

        condition = self.parse_expression()

        body = self.parse_block_statement()

        return WhileStatement(
            condition=condition,
            body=body,
            line=while_token.line,
            column=while_token.column,
        )

    def is_range_loop(self):
        pos = self.position

        while pos < len(self.tokens):
            token = self.tokens[pos]

            if token.type in (
                TokenType.RANGE_EXCLUSIVE,
                TokenType.RANGE_INCLUSIVE,
            ):
                return True

            if token.type == TokenType.LBRACE:
                return False

            pos += 1

        return False

    def parse_for_statement(self):
        if self.is_range_loop():
            return self.parse_for_range_statement()

        return self.parse_for_each_statement()

    def parse_for_range_statement(self):
        for_token = self.consume(TokenType.FOR)

        variable_token = self.consume(TokenType.IDENTIFIER)

        self.consume(TokenType.IN)

        start = self.parse_expression()

        range_token = self.current_token

        if range_token is None:
            raise UnexpectedEOFError(
                "Expected range operator.",
                variable_token.line,
                variable_token.column,
            )

        if range_token.type == TokenType.RANGE_EXCLUSIVE:
            inclusive = False
            self.advance()

        elif range_token.type == TokenType.RANGE_INCLUSIVE:
            inclusive = True
            self.advance()

        else:
            raise UnexpectedTokenError(
                "Expected range operator.",
                range_token.line,
                range_token.column,
            )

        end = self.parse_expression()

        body = self.parse_block_statement()

        return ForRangeStatement(
            variable_name=variable_token.value,
            start=start,
            end=end,
            inclusive=inclusive,
            body=body,
            line=for_token.line,
            column=for_token.column,
        )

    def parse_for_each_statement(self):
        for_token = self.consume(TokenType.FOR)

        variable_token = self.consume(TokenType.IDENTIFIER)

        self.consume(TokenType.IN)

        iterable = self.parse_expression()

        body = self.parse_block_statement()

        return ForEachStatement(
            variable_name=variable_token.value,
            iterable=iterable,
            body=body,
            line=for_token.line,
            column=for_token.column,
        )

    def parse_break_statement(self):
        token = self.consume(TokenType.BREAK)

        return BreakStatement(
            line=token.line,
            column=token.column,
        )

    def parse_continue_statement(self):
        token = self.consume(TokenType.CONTINUE)

        return ContinueStatement(
            line=token.line,
            column=token.column,
        )

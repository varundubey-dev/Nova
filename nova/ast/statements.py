from nova.ast.base import Statement


class Program(Statement):
    def __init__(
        self,
        statements,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.statements = statements

    def __repr__(self):
        return f"Program({self.statements})"


class VariableDeclaration(Statement):
    def __init__(
        self,
        name,
        var_type,
        value=None,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.name = name
        self.var_type = var_type
        self.value = value

    def __repr__(self):
        return (
            f"VariableDeclaration("
            f"name={self.name!r}, "
            f"var_type={self.var_type!r}, "
            f"value={self.value}"
            f")"
        )


class ConstantDeclaration(Statement):
    def __init__(
        self,
        name,
        const_type,
        value=None,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.name = name
        self.const_type = const_type
        self.value = value

    def __repr__(self):
        return (
            f"ConstantDeclaration("
            f"name={self.name!r}, "
            f"const_type={self.const_type!r}, "
            f"value={self.value}"
            f")"
        )


class Assignment(Statement):
    def __init__(
        self,
        name,
        value,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.name = name
        self.value = value

    def __repr__(self):
        return f"Assignment(" f"name={self.name!r}, " f"value={self.value}" f")"


class ArrayAssignment(Statement):
    def __init__(
        self,
        target,
        value,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.target = target
        self.value = value

    def __repr__(self):
        return f"ArrayAssignment(" f"target={self.target}, " f"value={self.value}" f")"


class SchemaDeclaration(Statement):
    def __init__(
        self,
        name,
        schema,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.name = name
        self.schema = schema

    def __repr__(self):
        return (
            f"SchemaDeclaration(" f"name={self.name!r}, " f"schema={self.schema}" f")"
        )


class PropertyAssignment(Statement):
    def __init__(
        self,
        target,
        value,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.target = target
        self.value = value

    def __repr__(self):
        return (
            f"PropertyAssignment(" f"target={self.target}, " f"value={self.value}" f")"
        )


class PrintStatement(Statement):
    def __init__(
        self,
        expressions,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.expressions = expressions

    def __repr__(self):
        return f"PrintStatement({self.expressions})"


class BlockStatement(Statement):
    def __init__(
        self,
        statements,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.statements = statements

    def __repr__(self):
        return f"BlockStatement({self.statements})"


class IfStatement(Statement):
    def __init__(
        self,
        condition,
        then_branch,
        else_branch=None,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def __repr__(self):
        return (
            f"IfStatement("
            f"condition={self.condition}, "
            f"then_branch={self.then_branch}, "
            f"else_branch={self.else_branch}"
            f")"
        )


class WhileStatement(Statement):
    def __init__(
        self,
        condition,
        body,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.condition = condition
        self.body = body

    def __repr__(self):
        return (
            f"WhileStatement(" f"condition={self.condition}, " f"body={self.body}" f")"
        )


class ForRangeStatement(Statement):
    def __init__(
        self,
        variable_name,
        start,
        end,
        inclusive,
        body,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.variable_name = variable_name
        self.start = start
        self.end = end
        self.inclusive = inclusive
        self.body = body

    def __repr__(self):
        return (
            f"ForRangeStatement("
            f"variable_name={self.variable_name!r}, "
            f"start={self.start}, "
            f"end={self.end}, "
            f"inclusive={self.inclusive}, "
            f"body={self.body}"
            f")"
        )


class ForEachStatement(Statement):
    def __init__(
        self,
        variable_name,
        iterable,
        body,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.variable_name = variable_name
        self.iterable = iterable
        self.body = body

    def __repr__(self):
        return (
            f"ForEachStatement("
            f"variable_name={self.variable_name!r}, "
            f"iterable={self.iterable}, "
            f"body={self.body}"
            f")"
        )


class BreakStatement(Statement):
    def __init__(
        self,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

    def __repr__(self):
        return "BreakStatement()"


class ContinueStatement(Statement):
    def __init__(
        self,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

    def __repr__(self):
        return "ContinueStatement()"

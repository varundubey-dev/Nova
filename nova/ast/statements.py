from nova.ast.base import Statement, Node


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
        self, name, var_type, value=None, line=None, column=None, exported=False
    ):
        super().__init__(line, column)

        self.name = name
        self.var_type = var_type
        self.value = value
        self.exported = exported

    def __repr__(self):
        return (
            f"VariableDeclaration("
            f"name={self.name!r}, "
            f"var_type={self.var_type!r}, "
            f"value={self.value}, "
            f"exported={self.exported}"
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
        exported=False,
    ):
        super().__init__(line, column)

        self.name = name
        self.const_type = const_type
        self.value = value
        self.exported = exported

    def __repr__(self):
        return (
            f"ConstantDeclaration("
            f"name={self.name!r}, "
            f"const_type={self.const_type!r}, "
            f"value={self.value}, "
            f"exported={self.exported}"
            f")"
        )


class FunctionDeclaration(Statement):
    def __init__(
        self,
        name,
        parameters,
        body,
        return_type=None,
        line=None,
        column=None,
        exported=False,
    ):
        super().__init__(line, column)

        self.name = name
        self.parameters = parameters
        self.body = body
        self.return_type = return_type
        self.exported = exported

    def __repr__(self):
        return (
            f"FunctionDeclaration("
            f"name={self.name!r}, "
            f"parameters={self.parameters}, "
            f"return_type={self.return_type!r}, "
            f"exported={self.exported}, "
            f"body={self.body}"
            f")"
        )


class Parameter(Node):
    def __init__(
        self,
        name,
        parameter_type,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.name = name
        self.parameter_type = parameter_type

    def __repr__(self):
        return (
            f"Parameter("
            f"name={self.name!r}, "
            f"parameter_type={self.parameter_type!r}"
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
        exported=False,
    ):
        super().__init__(line, column)

        self.name = name
        self.schema = schema
        self.exported = exported

    def __repr__(self):
        return (
            f"SchemaDeclaration("
            f"name={self.name!r}, "
            f"schema={self.schema}, "
            f"exported={self.exported}"
            f")"
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


class ReturnStatement(Statement):
    def __init__(
        self,
        value=None,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.value = value

    def __repr__(self):
        return f"ReturnStatement(" f"value={self.value}" f")"


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

class ImportStatement(Statement):
    def __init__(
        self,
        module_path,
        imports=None,
        alias=None,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.module_path = module_path
        self.imports = imports
        self.alias = alias

    def __repr__(self):
        return (
            f"ImportStatement("
            f"module_path={self.module_path}, "
            f"imports={self.imports}, "
            f"alias={self.alias!r}"
            f")"
        )

class ImportItem(Node):
    def __init__(
        self,
        name,
        alias=None,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.name = name
        self.alias = alias

    def __repr__(self):
        return (
            f"ImportItem("
            f"name={self.name!r}, "
            f"alias={self.alias!r}"
            f")"
        )
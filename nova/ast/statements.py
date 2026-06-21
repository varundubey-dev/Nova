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


class PrintStatement(Statement):
    def __init__(
        self,
        expression,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.expression = expression

    def __repr__(self):
        return f"PrintStatement({self.expression})"

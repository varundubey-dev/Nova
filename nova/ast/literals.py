from nova.ast.base import Expression


class NumberLiteral(Expression):
    def __init__(
        self,
        value,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.value = value

    def __repr__(self):
        return f"NumberLiteral({self.value})"


class StringLiteral(Expression):
    def __init__(
        self,
        value,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.value = value

    def __repr__(self):
        return f"StringLiteral({self.value!r})"


class BooleanLiteral(Expression):
    def __init__(
        self,
        value,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.value = value

    def __repr__(self):
        return f"BooleanLiteral({self.value})"


class NullLiteral(Expression):
    def __init__(
        self,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

    def __repr__(self):
        return "NullLiteral()"


class ArrayLiteral(Expression):
    def __init__(
        self,
        elements,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.elements = elements

    def __repr__(self):
        return f"ArrayLiteral({self.elements})"

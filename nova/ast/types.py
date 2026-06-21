from nova.ast.base import Node


class ArrayType(Node):
    def __init__(
        self,
        element_types,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.element_types = element_types

    def __repr__(self):
        return f"ArrayType({self.element_types})"
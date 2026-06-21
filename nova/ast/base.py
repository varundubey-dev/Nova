class Node:
    def __init__(
        self,
        line=None,
        column=None,
    ):
        self.line = line
        self.column = column


class Statement(Node):
    def __init__(
        self,
        line=None,
        column=None,
    ):
        super().__init__(line, column)


class Expression(Node):
    def __init__(
        self,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

class NovaError(Exception):
    def __init__(
        self,
        message,
        line=None,
        column=None,
    ):
        super().__init__(message)

        self.message = message
        self.line = line
        self.column = column

    def __str__(self):
        if (
            self.line is not None
            and self.column is not None
        ):
            return (
                f"{self.message} "
                f"(line {self.line}, column {self.column})"
            )

        return self.message
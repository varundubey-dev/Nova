class RuntimeValue:
    def __init__(self, value):
        self.value = value


class NumberValue(RuntimeValue):
    def __repr__(self):
        return f"NumberValue({self.value})"


class StringValue(RuntimeValue):
    def __repr__(self):
        return f"StringValue({self.value!r})"


class BooleanValue(RuntimeValue):
    def __repr__(self):
        return f"BooleanValue({self.value})"


class NullValue(RuntimeValue):
    def __init__(self):
        super().__init__(None)

    def __repr__(self):
        return "NullValue()"

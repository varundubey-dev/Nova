class RuntimeValue:
    def __init__(self, value):
        self.value = value

    @property
    def type_name(self):
        return self.__class__.__name__


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


class ArrayValue(RuntimeValue):
    def __init__(self, elements):
        super().__init__(elements)

    def __repr__(self):
        return f"ArrayValue({self.value})"


class SchemaValue(RuntimeValue):
    def __init__(self, fields):
        super().__init__(fields)

    def __repr__(self):
        return f"SchemaValue({self.value})"


class MapValue(RuntimeValue):
    def __init__(self, properties):
        super().__init__(properties)

    def __repr__(self):
        return f"MapValue({self.value})"


class FunctionValue(RuntimeValue):
    def __init__(self, name, parameters, body, return_type, closure, is_stdlib=False):
        super().__init__(None)

        self.name = name
        self.parameters = parameters
        self.body = body
        self.return_type = return_type
        self.closure = closure
        self.is_stdlib = is_stdlib

    def __repr__(self):
        return f"FunctionValue(" f"{self.name}" f")"


class ModuleValue(RuntimeValue):
    def __init__(
        self,
        name,
        exports,
        path=None,
        is_stdlib=False,
    ):
        super().__init__(exports)

        self.name = name
        self.path = path
        self.is_stdlib = is_stdlib

    @property
    def exports(self):
        return self.value

    def __repr__(self):
        return (
            f"ModuleValue("
            f"name={self.name!r}, "
            f"exports={list(self.exports.keys())}"
            f")"
        )

from nova.interpreter.expressions import ExpressionInterpreter

from nova.interpreter.runtime_values import (
    NumberValue,
    ArrayValue,
)

from nova.ast import (
    Identifier,
    ArrayAccess,
)

from nova.errors import (
    InvalidArrayAccessError,
    InvalidArrayIndexError,
    InvalidArrayAssignmentError,
    DatatypeMismatchError,
    ConstantReassignmentError,
)


class ArrayInterpreter(ExpressionInterpreter):

    # -------------------------
    # Array Literals
    # -------------------------

    def visit_array_literal(self, node):
        elements = []

        for element in node.elements:
            elements.append(self.visit(element))

        return ArrayValue(elements)

    # -------------------------
    # Array Access
    # -------------------------

    def visit_array_access(self, node):
        array = self.visit(node.array)

        if not isinstance(
            array,
            ArrayValue,
        ):
            raise InvalidArrayAccessError(
                "Cannot index non-array value.",
                node.line,
                node.column,
            )

        index = self.visit(node.index)

        if not isinstance(
            index,
            NumberValue,
        ):
            raise InvalidArrayIndexError(
                "Array index must be numeric.",
                node.line,
                node.column,
            )

        if not isinstance(
            index.value,
            int,
        ):
            raise InvalidArrayIndexError(
                "Array index must be an integer.",
                node.line,
                node.column,
            )
        try:
            return array.value[index.value]

        except IndexError:
            raise InvalidArrayIndexError(
                "Array index out of bounds.",
                node.line,
                node.column,
            )

    # -------------------------
    # Array Assignment
    # -------------------------

    def visit_array_assignment(self, node):
        target = node.target

        if not isinstance(
            target,
            ArrayAccess,
        ):
            raise InvalidArrayAssignmentError(
                "Invalid array assignment.",
                node.line,
                node.column,
            )

        root = self.get_array_root(target)

        if not isinstance(
            root,
            Identifier,
        ):
            raise InvalidArrayAssignmentError(
                "Invalid assignment target.",
                node.line,
                node.column,
            )

        variable_info = self.environment.get_variable_info(root.name)

        if variable_info["constant"]:
            raise ConstantReassignmentError(
                "Cannot modify immutable collection.",
                node.line,
                node.column,
            )

        array = self.visit(target.array)

        if not isinstance(
            array,
            ArrayValue,
        ):
            raise InvalidArrayAccessError(
                "Cannot index non-array value.",
                target.line,
                target.column,
            )
        index = self.visit(target.index)

        if not isinstance(
            index,
            NumberValue,
        ):
            raise InvalidArrayIndexError(
                "Array index must be numeric.",
                target.line,
                target.column,
            )
        if not isinstance(
            index.value,
            int,
        ):
            raise InvalidArrayIndexError(
                "Array index must be an integer.",
                target.line,
                target.column,
            )

        value = self.visit(node.value)

        declared_type = variable_info["type"]

        depth = self.get_array_depth(target)

        expected_type = self.get_element_type(
            declared_type,
            depth,
        )

        # Multi-type arrays
        if hasattr(
            expected_type,
            "element_types",
        ):
            valid = False

            for allowed_type in expected_type.element_types:
                try:
                    self.environment.validate_type(
                        allowed_type,
                        value,
                        node.line,
                        node.column,
                    )

                    valid = True
                    break

                except Exception:
                    pass

            if not valid:
                raise DatatypeMismatchError(
                    "Datatype mismatch.",
                    node.line,
                    node.column,
                )

        else:
            self.environment.validate_type(
                expected_type,
                value,
                node.line,
                node.column,
            )

        try:
            array.value[index.value] = value

        except IndexError:
            raise InvalidArrayIndexError(
                "Array index out of bounds.",
                target.line,
                target.column,
            )

        return value

    # -------------------------
    # Helpers
    # -------------------------

    def get_array_root(
        self,
        target,
    ):
        current = target

        while isinstance(
            current,
            ArrayAccess,
        ):
            current = current.array

        return current

    def get_element_type(
        self,
        array_type,
        depth,
    ):
        current = array_type

        for _ in range(depth):
            if not hasattr(
                current,
                "element_types",
            ):
                return current

            if len(current.element_types) > 1:
                return current

            current = current.element_types[0]

        return current

    def get_array_depth(
        self,
        target,
    ):
        depth = 0

        current = target

        while isinstance(
            current,
            ArrayAccess,
        ):
            depth += 1
            current = current.array

        return depth

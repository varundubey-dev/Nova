from pathlib import Path

from nova.modules.loader import ModuleLoader

from nova.errors import ModuleNotFoundError, CircularImportError


class ModuleResolver:
    def __init__(
        self,
        project_root=None,
        stdlib_root=None,
    ):
        self.project_root = (
            Path(project_root).resolve() if project_root is not None else Path.cwd()
        )

        self.stdlib_root = (
            Path(stdlib_root).resolve()
            if stdlib_root is not None
            else Path(__file__).resolve().parent.parent / "stdlibs"
        )

        self.loader = ModuleLoader(self)

        self.loading_stack = []

    def resolve(
        self,
        module_path,
    ):
        """
        module_path:

            ["math"]

            ["examples", "utils"]
        """

        if len(module_path) == 1:
            stdlib = self.stdlib_root / f"{module_path[0]}.nova"

            if stdlib.exists():
                return self._load(
                    stdlib,
                    module_path,
                    is_stdlib=True,
                )

        local = self.project_root.joinpath(*module_path).with_suffix(".nova")

        return self._load(
            local,
            module_path,
            is_stdlib=False,
        )

    def _load(
        self,
        path,
        module_path,
        is_stdlib,
    ):
        path = Path(path).resolve()

        if not path.exists():
            raise ModuleNotFoundError(f"Module '{'.'.join(module_path)}' not found.")

        key = str(path)

        if key in self.loading_stack:
            cycle = self.loading_stack[self.loading_stack.index(key) :] + [key]

            names = [Path(item).stem for item in cycle]

            raise CircularImportError(
                "Circular module dependency detected:\n\n" + " -> ".join(names)
            )

        self.loading_stack.append(key)

        try:
            module = self.loader.load(
                path,
                is_stdlib=is_stdlib,
            )
            return module

        finally:
            self.loading_stack.pop()

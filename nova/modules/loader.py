from pathlib import Path

from nova.pipeline import create_interpreter
from nova.interpreter.runtime_values import ModuleValue


class ModuleLoader:
    def __init__(self, resolver):
        self.resolver = resolver
        self.cache = {}

    def load(
        self,
        path,
        is_stdlib=False,
    ):
        module_path = str(Path(path).resolve())

        if module_path in self.cache:
            return self.cache[module_path]

        source = Path(module_path).read_text(encoding="utf-8")

        interpreter = create_interpreter(
            source,
            resolver=self.resolver,
            is_stdlib=is_stdlib,
        )

        module = ModuleValue(
            name=Path(module_path).stem,
            exports=interpreter.environment.get_exports(),
            path=module_path,
            is_stdlib=is_stdlib,
        )

        self.cache[module_path] = module

        return module

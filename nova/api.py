from nova.modules.resolver import ModuleResolver
from nova.pipeline import create_interpreter


def run_source(
    source: str,
    input_provider=input,
    project_root=None,
    output_callback=None,
):
    resolver = ModuleResolver(
        project_root=project_root,
    )

    interpreter = create_interpreter(
        source,
        input_provider=input_provider,
        resolver=resolver,
        output_callback=output_callback,
    )

    return interpreter.output


def run_file(
    path: str,
    input_provider=input,
    project_root=None,
    output_callback=None,
):
    with open(path, "r", encoding="utf-8") as file:
        source = file.read()

    output = run_source(
        source,
        input_provider=input_provider,
        project_root=project_root,
        output_callback=output_callback,
    )

    return source, output

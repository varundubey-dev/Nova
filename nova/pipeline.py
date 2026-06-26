from nova.lexer.lexer import Lexer
from nova.parser.parser import Parser
from nova.interpreter.interpreter import Interpreter


def create_interpreter(
    source: str,
    input_provider=None,
    resolver=None,
    is_stdlib=False,
):
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter(
        input_provider=input_provider,
        resolver=resolver,
        is_stdlib=is_stdlib,
    )

    interpreter.interpret(ast)

    return interpreter
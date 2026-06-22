from nova.lexer.lexer import Lexer
from nova.parser.parser import Parser
from nova.interpreter.interpreter import Interpreter


def run_source(source: str):
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter()
    interpreter.interpret(ast)

    return interpreter.output


def run_file(path: str):
    with open(path, "r", encoding="utf-8") as file:
        source = file.read()

    output = run_source(source)

    return source, output
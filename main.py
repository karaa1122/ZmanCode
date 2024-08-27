from lexer import Lexer, read_file
from parser import Parser, execute_python_code

def main():
    kurdish_code = read_file('main.ku')
    lexer = Lexer(kurdish_code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    python_code = parser.parse()

    execute_python_code(python_code)

if __name__ == "__main__":
    main()

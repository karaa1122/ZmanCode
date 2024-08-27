
class Lexer:
    def __init__(self, code):
        self.code = code
    
    def tokenize(self):
        tokens = []
        for lines in self.code:
            tokens.append(lines.split())
        
        return tokens


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.readlines()

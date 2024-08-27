class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.translations = {
            "agar": "if",
            "agareki_tr": "elif",
            "agar_na": "else",
            "chap": "print",
            "lo": "for",
            "ka": "while",
            "hala": "False",
            "rasta": "True"
        }
    
    def parse(self):
        python_code = []
        for token_list in self.tokens:
            python_line = ' '.join(self.translate_token(token) for token in token_list)
            python_code.append(python_line)
        return python_code
    
    def translate_token(self, token):
        return self.translations.get(token, token)

def execute_python_code(python_code):
    exec('\n'.join(python_code))

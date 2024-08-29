import ply.lex as lex
import ply.yacc as yacc

kurdish_to_python = {
    "agar": "if",
    "agareki_tr": "elif",
    "agar_na": "else",
    "chap": "print",
    "lo": "for",
    "ka": "while",
    "hala": "False",
    "rasta": "True",
    "in": "in",
    "range": "range"
}

# Define tokens
tokens = (
    'ID', 'STRING', 'LPAREN', 'RPAREN', 'COLON', 'EQ', 'LT', 'NUMBER', 'PLUS'
)

# Token patterns
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COLON   = r':'
t_STRING  = r'\".*?\"'
t_EQ      = r'='
t_LT      = r'<'
t_PLUS    = r'\+'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.value = kurdish_to_python.get(t.value, t.value)  # Translate Kurdish keywords
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Track declared variables
declared_variables = set()

# Parsing rules
def p_statement_expr(p):
    p[0] = p[1]

def p_declaration_statement(p):
    '''declaration_statement : ID EQ NUMBER'''
    var_name = p[1]
    declared_variables.add(var_name)
    p[0] = f"{var_name} = {p[3]}"

def p_if_statement(p):
    '''if_statement : ID expression COLON block'''
    p[0] = f"if {p[2]}:\n{p[4]}"

def p_elif_statement(p):
    '''elif_statement : ID expression COLON block'''
    p[0] = f"elif {p[2]}:\n{p[4]}"

def p_else_statement(p):
    '''else_statement : ID COLON block'''
    p[0] = f"else:\n{p[3]}"

def p_print_statement(p):
    '''print_statement : ID LPAREN STRING RPAREN'''
    p[0] = f"print({p[3]})"

def p_for_statement(p):
    '''for_statement : ID ID ID expression COLON block'''
    p[0] = f"for {p[2]} in {p[4]}:\n{p[6]}"

def p_while_statement(p):
    '''while_statement : ID expression COLON block'''
    p[0] = f"while {p[2]}:\n{p[4]}"


def p_assignment_statement(p):
    '''assignment_statement : ID EQ expression'''
    var_name = p[1]
    if var_name not in declared_variables:
        declared_variables.add(var_name)
    p[0] = f"{var_name} = {p[3]}"

def p_expression_condition(p):
    '''expression : ID LT ID'''
    p[0] = f"{p[1]} < {p[3]}"

def p_expression_range(p):
    '''expression : ID LPAREN ID RPAREN'''
    p[0] = f"{p[1]}({p[3]})"

def p_expression_simple(p):
    '''expression : ID
                  | NUMBER'''
    p[0] = p[1]

def p_expression_addition(p):
    '''expression : expression PLUS expression'''
    p[0] = f"{p[1]} + {p[3]}"

def p_block_statements(p):
    '''block : statement block
             | statement'''
    if len(p) == 3:
        p[0] = f"{p[1]}\n{p[2]}"
    else:
        p[0] = p[1]

def p_error(p):
    print("Syntax error")
    if p:
        print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

def translate_kurdish_to_python(code):
    global declared_variables
    declared_variables = set()
    python_code = parser.parse(code)
    return python_code

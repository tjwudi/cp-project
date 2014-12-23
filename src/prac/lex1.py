import ply.lex as lex

tokens = (
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'NEWLINE')

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print "Illegal '%s'" % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex();

data = '''
3 + 4 * 10
+ 20 * 2
'''

lexer.input(data)

while True:
    token = lexer.token()
    if not token: break
    print token



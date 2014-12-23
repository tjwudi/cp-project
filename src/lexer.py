import ply.lex as lex

tokens = (
    'H1OPEN',
    'H1CLOSE',
    'H2OPEN',
    'H2CLOSE',
    'PLAIN',
    'EMPTYLINES'
    )

states = (
    ('h1', 'exclusive'),
    ('h2', 'exclusive')
    )

# ANY
def t_ANY_PLAIN(t):
  r'[a-zA-Z0-9 ]+'
  return t

# INITIAL state
def t_EMPTYLINES(t):
  r'\n+'
  return t

def t_H2OPEN(t):
  r'\#{2}'
  t.lexer.push_state('h2')
  return t

def t_H1OPEN(t):
  r'\#'
  t.lexer.push_state('h1')
  return t


# h1 state
def t_h1_H1CLOSE(t):
  r'\n'
  t.lexer.pop_state()
  return t

# h2 state
def t_h2_H2CLOSE(t):
  r'\n'
  t.lexer.pop_state()
  return t

# Error handling
def t_ANY_error(t):
  print 'Token not identified: %s' % t

lexer = lex.lex()

'''
infile = open('prac/in1.md', 'r')
raw_content = infile.read()
lexer.input(raw_content)
while True:
    token = lexer.token()
    if not token:
        break
    print token
'''

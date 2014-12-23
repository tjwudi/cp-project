import ply.lex as lex


tokens = (
    'H1OPEN',
    'H1CLOSE',
    'PLAIN',
    )

states = (
    ('h1', 'exclusive'),
    )

def t_H1OPEN(t):
  r'\#'
  t.lexer.push_state('h1')
  return t

def t_h1_H1CLOSE(t):
  r'\n+'
  t.lexer.pop_state()
  return t

def t_ANY_PLAIN(t):
  r'[a-zA-Z0-9 ]+'
  return t

def t_h1_error(t):
  t.lexer.skip(1)

def t_error(t):
  t.lexer.skip(1)


lexer = lex.lex()


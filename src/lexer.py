import ply.lex as lex

tokens = (
    'HR',
    'H1OPEN',
    'H1CLOSE',
    'H2OPEN',
    'H2CLOSE',
    'H3OPEN',
    'H3CLOSE',
    'ICOPEN',
    'ICCLOSE',
    'PLAIN',
    'BLOCKDIV',
    'STRONGOPEN',
    'STRONGCLOSE',
    'ITALICOPEN',
    'ITALICCLOSE',
    )

states = (
        ('h1', 'exclusive'),
        ('h2', 'exclusive'),
        ('h3', 'exclusive'),
        ('hr', 'exclusive'),
        )

# hr
def t_HR(t):
  r'===\n|\-\-\-\n|\*\ \*\ \*\n'
  return t

# strong
def t_STRONG(t):
  r'(\*|\_){2}'
  if len(t.lexer.inline_stack) > 0 and t.lexer.inline_stack[-1] == 'strong':
    t.type = 'STRONGCLOSE'
    t.lexer.inline_stack.pop()
  else:
    t.type = 'STRONGOPEN'
    t.lexer.inline_stack.append('strong')
  return t

# italic
def t_ITALIC(t):
  r'(\*|\_){1}'
  if len(t.lexer.inline_stack) > 0 and t.lexer.inline_stack[-1] == 'italic':
    t.type = 'ITALICCLOSE'
    t.lexer.inline_stack.pop()
  else:
    t.type = 'ITALICOPEN'
    t.lexer.inline_stack.append('italic')
  return t

# inline code - IC
def t_IC(t):
  r'`'
  if len(t.lexer.inline_stack) > 0 and t.lexer.inline_stack[-1] == 'inline-code':
    t.type = 'ICOPEN'
    t.lexer.inline_stack.pop()
  else:
    t.type = 'ICCLOSE'
    t.lexer.inline_stack.append('inline-code')
  return t

# h3 
def t_H3OPEN(t):
  r'\#{3}'
  t.lexer.push_state('h3')
  return t

def t_h3_H3CLOSE(t):
  r'\b'
  t.lexer.pop_state()
  return t


# h2 
def t_H2OPEN(t):
  r'\#{2}'
  t.lexer.push_state('h2')
  return t

def t_h2_H2CLOSE(t):
  r'\b'
  t.lexer.pop_state()
  return t

# h1
def t_H1OPEN(t):
  r'\#'
  t.lexer.push_state('h1')
  return t

def t_h1_H1CLOSE(t):
  r'\b'
  t.lexer.pop_state()
  return t

# ANY
def t_ANY_PLAIN(t):
  r'[a-zA-Z0-9\,\.\' ]+'
  return t

# empty lines
def t_BLOCKDIV(t):
  r'\n+'
  return t


# Error handling
def t_ANY_error(t):
  print 'Token not identified: %s' % t

lexer = lex.lex(debug=1)
lexer.inline_stack = []

infile = open('../inputs/input1.md', 'r')
raw_content = infile.read()
lexer.input(raw_content)
while True:
    token = lexer.token()
    if not token:
        break
    print token

import ply.yacc as yacc

from lexer import tokens

#
# article
#

def p_article_block(p):
  'article : article block'
  p[0] = p[1] + p[2]

def p_article_empty(p):
  'article :'
  p[0] = ''
  pass

#
# block
#

def p_block_h1(p):
  'block : h1'
  p[0] = p[1]

def p_block_h2(p):
  'block : h2'
  p[0] = p[1]

#
# Inline
#
def p_inline_plain(p):
  'inline : PLAIN'
  p[0] = p[1]

#
# h1
#
def p_h1(p):
  'h1 : H1OPEN inline H1CLOSE'
  p[0] = '<h1>%s</h1>' % p[2].strip()

#
# h2
#
def p_h2(p):
  'h2 : H2OPEN PLAIN H2CLOSE'
  p[0] = '<h2>%s</h2>' % p[2].strip()


parser = yacc.yacc()
infile = open('prac/in1.md', 'r')
raw_content = infile.read()
compiled_content = parser.parse(raw_content)
print compiled_content

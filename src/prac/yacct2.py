import ply.yacc as yacc

from lext2 import tokens

def p_h1(p):
  'h1 : H1OPEN plain H1CLOSE'
  p[0] = '<h1>%s</h1>' % p[2]

def p_plain(p):
  'plain : PLAIN'
  p[0] = p[1]

parser = yacc.yacc()

infile = open('in1.md', 'r')
raw_content = infile.read()
result = parser.parse(raw_content)

outfile = open('out1.md', 'w')
outfile.write(result)

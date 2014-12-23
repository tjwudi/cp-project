import ply.yacc as yacc

from lexer import tokens


#
# article
#

def p_article_block(p):
  'article : block article'
  p[0] = p[1] + p[2]

def p_article_empty(p):
  'article :'
  p[0] = ''
  pass
  
#
# block
#

def p_block(p):
  '''
  block : BLOCKDIV
        | h1
        | h2
        | h3
        | hr
        | paragraph
  '''
  p[0] = p[1]


#
# paragraph
#
def p_paragraph(p):
  'paragraph : inline'
  p[0] = '<p>%s</p>' % p[1]

#
# Inline
#

def p_inline(p):
  '''
  inline : inline PLAIN
         | inline strong
         | inline italic
         | inline inline-code
  '''
  p[0] = p[1] + p[2]


def p_inline_empty(p):
  'inline :'
  p[0] = ''
  pass

#
# h1
#
def p_h1(p):
  'h1 : H1OPEN PLAIN H1CLOSE'
  p[0] = '<h1>%s</h1>' % p[2].strip()

#
# h2
#
def p_h2(p):
  'h2 : H2OPEN PLAIN H2CLOSE'
  p[0] = '<h2>%s</h2>' % p[2].strip()

#
# h3
#
def p_h3(p):
  'h3 : H3OPEN PLAIN H3CLOSE'
  p[0] = '<h3>%s</h3>' % p[2].strip()

#
# hr
#
def p_hr(p):
  'hr : HR'
  p[0] = '<hr/>'

#
# strong
#
def p_strong(p):
  'strong : STRONGOPEN inline STRONGCLOSE'
  p[0] = '<strong>%s</strong>' % p[2]

#
# italic
#
def p_italic(p):
  'italic : ITALICOPEN PLAIN ITALICCLOSE'
  p[0] = '<i>%s</i>' % p[2]

#
# inline code
#
def p_inline_code(p):
  'inline-code : ICOPEN PLAIN ICCLOSE'
  p[0] = '<code>%s</code>' % p[2]

#
# Error handling
#
def p_error(p):
  print 'Syntax error: %s' % p

parser = yacc.yacc()
infile = open('../inputs/input1.md', 'r')
raw_content = infile.read()
compiled_content = parser.parse(raw_content)

templatefile = open('template.html', 'r')
template_content = templatefile.read()
output_content = template_content.replace('!yield!', compiled_content)

outputfile = open('index.html', 'w')
outputfile.write(output_content)
print output_content

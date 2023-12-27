import ply.yacc as yacc

from lex import tokens

# Parsing rules
def p_program(p):
    'program : statements'
    p[0] = p[1]

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:  # single statement
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : INSTRUCTION
                 | INSTRUCTION operands
                 | INSTRUCTION operands DBLCOLON INSTRUCTION operands
    '''
    if len(p) == 2 or len(p) == 3:
      p[0] = [p[1], p[2]] if len(p) == 3 else p[1]
    else:
      p[0] = (p[1], p[2], p[4], p[5])

def p_operands(p):
    '''operands : operand
                | operands COMMA operand
                | operands OR operand
                | operands operand'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = p[1] + [p[3]]

def p_operand(p):
    '''operand : SGPR 
               | VGPR 
               | INTEGER 
               | FLOATING
               | SYMBOL
               | BINARY
               | func
               | modifier'''
    p[0] = p[1]

def p_modifier(p):
    '''modifier : LABEL INTEGER'''
    p[0] = (p[1], p[2])
  
def p_func(p):
  ''' func : SYMBOL LPAREN SYMBOL RPAREN
           | SYMBOL LPAREN INTEGER RPAREN'''
  p[0] = [p[1], p[3]]


def p_error(p):
    print(p)
    print(f"Syntax error at '{p.value}'")

# Build the parser
parser = yacc.yacc(debug=True)
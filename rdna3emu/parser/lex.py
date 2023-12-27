import ply.lex as lex

reserved = {
    '.set' : 'SET',
    '.globl' : 'GLOBAL',
    '.rodata' : 'KERNEL_DESC',
    '.data' : 'DATA',
    '.bss' : 'BSS',
    'SHN_AMDGPU_LDS': 'LDS_GLOBAL',
    'vcc_lo' : 'VCC_LO',
    'vcc_hi' : 'VCC_HI',
    'm0' : 'M0',
}
# List of token names
tokens =  ( 
   'TEXT',
   'TARGET',
   'WEAK',
   'P2ALIGN',
   'TYPE',   
   'DIRECTIVE',
   'INTEGER',
   'HEX',
   'OCTAL',
   'BINARY',
   'FLOATING',
   'VGPR',
   'SGPR',
   'SYMBOL',
   'LABEL',
   'INSTRUCTION',
   'COMMA',
   'DBLCOLON',
   'COMMENT',
   'STRING',
   'LPAREN',
   'RPAREN', 'PLUS', 'MINUS', 'AT', 'OR', 'HASH',
   'REF',
) + tuple(reserved.values())

# Regular expression rules for simple tokens
decimal = r'[-]?[1-9][0-9]*|0'
hex = r'[-]?0x[0-9a-fA-F]+ | [-]?[0x]?[0-9][0-9a-fA-F]*[hH]'
octal  = r'[-]?0[0-7]+'
binary = r'[-]?0b[01]+'
integer =hex + r'|' +  octal + r'|' + binary + r'|' +  decimal 
t_INTEGER = integer
t_FLOATING = r'[-]?[0-9]*[.][0-9]+([eE][+-]?[0-9]*)? | [-]0x[0-9a-fA-F]*(.[0-9a-fA-F]+)?[pP][+-]?[0-9a-fA-F]+'
t_DBLCOLON = r'::'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_AT = r'@'
t_OR = r'\|'
t_HASH = r'\#'

def t_REF(t):
  r'<[a-zA-Z_.][a-zA-Z0-9_$.@]*>'
  return t
def t_TEXT(t): 
  r'\.text'
  return t
def t_TARGET(t): 
  r'\.amdgcn_target'
  return t
def t_WEAK(t):
  r'\.weak'
  return t
def t_P2ALIGN(t):
  r'\.p2align'
  return t
def t_TYPE(t):
  r'\.type'
  return t
def t_COMMA(t):
  r','
  return t
def t_DIRECTIVE(t):
  r'\.[a-zA-Z_]+'
  return t

def t_VGPR(t):
  r'v\d+|v\[\d+:\d+\]|v\[\d+\]'  
  return t

def t_SGPR(t):
  r's\d+|s\[\d+:\d+\]|s\[\d+\]'  
  return t

def t_INSTRUCTION(t):
    r's_[a-zA-Z_\d+]+|v_[a-zA-Z_\d+]+'
    return t
  
def t_STRING(t):
    r'\"[^"]*\"'
    return t
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_LABEL(t):
    r'[a-zA-Z_.][a-zA-Z0-9_$.@]*:'
    return t

def t_SYMBOL(t):
   r'[a-zA-Z_.][a-zA-Z0-9_$.@]*'
   t.type = reserved.get(t.value,'SYMBOL')
   return t


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# A rule to handle comments
def t_COMMENT(t):
    r'\/\/.*'
    pass  # Token discarded

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# with open('../../Data/tinyconvdump.txt', 'r') as f:
#   for _ in range(5):
#      next(f)
#   data = f.read() 
# # Test it out with the file contents
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     print(tok)

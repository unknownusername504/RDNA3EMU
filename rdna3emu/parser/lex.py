import ply.lex as lex
import rdna3emu.parser.ir as ir

reserved = {
    ".set": "SET",
    ".globl": "GLOBAL",
    ".rodata": "KERNEL_DESC",
    ".data": "DATA",
    ".bss": "BSS",
    "SHN_AMDGPU_LDS": "LDS_GLOBAL",

}
# List of token names
tokens = (
    "TEXT",
    "TARGET",
    "WEAK",
    "P2ALIGN",
    "TYPE",
    "DIRECTIVE",
    "INTEGER",
    "HEX",
    "OCTAL",
    "DECIMAL",
    "BINARY",
    "FLOATING",
    "VGPR",
    "SGPR",
    "SYMBOL",
    "LABEL",
    "INSTRUCTION",
    "COMMA",
    "DBLCOLON",
    "COMMENT",
    "STRING",
    "LPAREN",
    "RPAREN",
    "PLUS",
    "MINUS",
    "AT",
    "OR",
    "HASH",
    "REF",
    "EXEC_LO", "EXEC_HI",
    "VCC_LO", "VCC_HI"
) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_DBLCOLON = r"::"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_PLUS = r"\+"
t_MINUS = r"-"
t_AT = r"@"
t_OR = r"\|"
t_HASH = r"\#"

'''
    "vcc_lo": "VCC_LO" ,
    "vcc_hi": "VCC_HI", 
    "exec_lo": "EXEC_LO",
    "exec_hi": "EXEC_HI", 
    "m0": "M0",
'''



def t_HEX(t):
    r"[-]?0x[0-9a-fA-F]+ | [-]?[0x]?[0-9][0-9a-fA-F]*[hH]"
    t.value = ir.Operand(type="Hex", value=int(t.value, base=16))
    return t


def t_OCTAL(t):
    r"[-]?0[0-7]+"
    t.value = ir.Operand(type="Octal", value=int(t.value, base=8))
    return t


def t_BINARY(t):
    r"[-]?0b[01]+"
    t.value = ir.Operand(type="Binary", value=int(t.value, base=2))
    return t

def t_FLOATING(t):
    r"[-]?[0-9]*[.][0-9]+([eE][+-]?[0-9]*)? | [-]0x[0-9a-fA-F]*(.[0-9a-fA-F]+)?[pP][+-]?[0-9a-fA-F]+"
    t.value = ir.Operand(type="Float", value=float(t.value))
    return t

def t_DECIMAL(t):
    r"[-]?[1-9][0-9]*|0"
    t.value = ir.Operand(type="Decimal", value=int(t.value))
    return t

def t_EXEC_LO(t):
  r"exec_lo"
  t.value = ir.Operand(type="EXEC_LO", value=t.value)
  return t

def t_EXEC_HI(t):
  r"exec_hi"
  t.value = ir.Operand(type="EXEC_HI", value=t.value)
  return t

def t_VCC_LO(t):
  r"vcc_lo"
  t.value = ir.Operand(type="VCC_LO", value=t.value)
  return t

def t_VCC_HI(t):
  r"vccc_hi"
  t.value = ir.Operand(type="VCC_HI", value=t.value)
  return t

def t_REF(t):
    r"<[a-zA-Z_.][a-zA-Z0-9_$.@]*>"
    return t


def t_TEXT(t):
    r"\.text"
    return t


def t_TARGET(t):
    r"\.amdgcn_target"
    return t


def t_WEAK(t):
    r"\.weak"
    return t


def t_P2ALIGN(t):
    r"\.p2align"
    return t


def t_TYPE(t):
    r"\.type"
    return t


def t_COMMA(t):
    r","
    return t


def t_DIRECTIVE(t):
    r"\.[a-zA-Z_]+"
    return t


def t_VGPR(t):
    r"v\d+|v\[\d+:\d+\]|v\[\d+\]"
    t.value = ir.Operand(type="VGPR", value=t.value)
    return t


def t_SGPR(t):
    r"s\d+|s\[\d+:\d+\]|s\[\d+\]"
    t.value = ir.Operand(type="SGPR", value=t.value)
    return t


def t_INSTRUCTION(t):
    r"s_[a-zA-Z_\d+]+|v_[a-zA-Z_\d+]+|global_[a-zA-Z_\d+]+|ds_[a-zA-Z_\d+]+"
    instruction_func = lambda x: x
    # Get the instruction type
    instr = ir.Instruction(t.value)
    t.value = instr
    return t


def t_STRING(t):
    r'\"[^"]*\"'
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_LABEL(t):
    r"[a-zA-Z_.][a-zA-Z0-9_$.@]*:"
    return t


def t_SYMBOL(t):
    r"[a-zA-Z_.][a-zA-Z0-9_$.@]*"
    t.type = reserved.get(t.value, "SYMBOL")
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"


# A rule to handle comments
def t_COMMENT(t):
    r"\/\/.*"
    pass  # Token discarded


# Error handling rule
def t_error(t):
    # print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

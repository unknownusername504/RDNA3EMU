from rdna3emu.parser.yacc import parser
from rdna3emu.parser.lex import lexer


def parse(data, debug=False):
    return parser.parse(data, debug=debug, lexer=lexer)

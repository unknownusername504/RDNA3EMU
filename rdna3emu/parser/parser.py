from .yacc import parser
from .lex import lexer


def parse(data, debug=False):
    return parser.parse(data, debug=debug, lexer=lexer)

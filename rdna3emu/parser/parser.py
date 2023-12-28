import yacc
import lex
import pprint

# RUN from package root
# PYTHONPATH='.' python3 rdna3emu/parser/parser.py > parse.out
def parse():
  with open('Data/tinyconvdump.txt', 'r') as f:
    for _ in range(6):
      next(f)
    data = f.read() 
    return yacc.parser.parse(data, debug=True, lexer=lex.lexer)

if __name__ == '__main__':
  result = parse()
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(result)
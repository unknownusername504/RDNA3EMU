import yacc
import lex

def parse():
  with open('../../Data/tinyconvdump.txt', 'r') as f:
    for _ in range(6):
      next(f)
    data = f.read() 
    return yacc.parser.parse(data, debug=True, lexer=lex.lexer)

if __name__ == '__main__':
  result = parse()
  print(result)
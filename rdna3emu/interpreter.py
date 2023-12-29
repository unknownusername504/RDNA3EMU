
def interpret(stmts):
  for stmt in stmts:
    if isinstance(stmt, list):
      instr = stmt[0]
      operands = stmt[1:]
      print(instr, operands)
    else:
      print(stmt)
     
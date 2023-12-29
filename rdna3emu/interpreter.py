from rdna3emu.parser.ir import Instruction

class Clause:
  def __init__(self, length, simm16):
    self.executable = []
    self.length = length 
    self.simm16 = simm16 
  def __repr__(self):
    return f'Clause[len={self.length} instr={self.executable} simm16={self.simm16}]'

def build_executable(stmts):
  exec = []
  clause = None 
  i = 0
  while i < len(stmts):
    stmt = stmts[i]
    if isinstance(stmt, list):
      instr = stmt[0]
      operands = stmt[1:]
      # s_clause instr
      if instr.clause:
        simm16 = operands[0][0].value
        length = (simm16 & 0x3F) + 1
        clause = Clause(length=length, simm16=simm16)
        clause_instr = stmts[i+1:i+1+length]
        for instr_op in clause_instr:
          if isinstance(instr_op, list):
            executable = extract_exec(instr_op[0], instr_op[1:])
          else:
            executable = instr_op.fx
          clause.executable.append(executable)
        i += 1 + length
        exec.append(clause)
      else:
        if instr.name.startswith('V_DUAL'):
          next_operands = []
          for j, oper in enumerate(operands):
            if isinstance(oper, Instruction): 
              exec.append(extract_exec(instr, next_operands))
              exec.append(extract_exec(oper, operands[j+1:]))
              break
            else:
              next_operands.append(oper)
        else:
          r = extract_exec(instr, operands)
          if r:
            exec.append(r)
        i+=1
    else:
     exec.append(stmt.fx)
     i+=1
  return exec


ignore_instr = {'S_DELAY_ALU', 'S_WAITCNT', 'S_SENDMSG'}

def extract_exec(instr, operands):
  if instr.name in ignore_instr:
    return
  args = [] 
  for operand in operands:
    # TODO: Deal with null and operand strings
    if isinstance(operand, str): 
      continue
    if isinstance(operand, list):
      for sub_operand in operand: 
        if isinstance(sub_operand, tuple):
          # Offsets
          args.append(sub_operand[1].value)
        elif isinstance(sub_operand, str):
          continue
        elif sub_operand.registers:
          for reg in sub_operand.registers: args.append(int(reg[1:]))
        else:
          args.append(sub_operand.value)
    else:
        if operand.registers:
          for reg in operand.registers: args.append(int(reg[1:]))
        else:
          args.append(operand.value)
  
  return (instr.fx, args)

def run(executable):    
  for instr in executable:
    if isinstance(instr, Clause):
      for clause_instr, args in instr.executable:
        clause_instr(*args)
    else:
      instr[0](*instr[1])
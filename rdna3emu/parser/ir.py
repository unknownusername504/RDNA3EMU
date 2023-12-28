from rdna3emu.isa.instruction_set import InstructionSet
isa = InstructionSet()
class Operand:
  def __init__(self, type, value):
    self.type = type
    self.value = value
    self.registers = []
    if type == 'SGPR' or type == 'VGPR':
      self.preprocess_register_token()
    else:
       pass
    
  def preprocess_register_token(self):
      token_str = str(self.value)
      # Expand registers with array format [x:y] to individual registers
      if "[" in token_str:
          # Get the register name
          register_name = token_str.split("[")[0]
          # Get the register range
          register_range = token_str.split("[")[1][:-1]
          # Get the start and end of the range
          start, end = register_range.split(":")
          # Convert to integers
          start = int(start)
          end = int(end)
          # Add the registers to the tokens list
          for i in range(start, end + 1):
            self.registers.append(register_name + str(i))
      else:
          self.registers.append(token_str)

  def __repr__(self) -> str:
    if self.type in ['VGPR', 'SGPR']:
      return f'Operand[type={self.type}, registers={self.registers}]'

    return f'Operand[type={self.type}, value={self.value}]'


class Instruction:
  def __init__(self, op):
        # Convert to uppercase string
      instr = op.upper()
      self.name = instr
      # The register array parsing will mean we should treat anything higher than 1 dword as 1 dword ops
      # so we can just set the size part of the instruction to 32
      if "64" in instr:
          instr = instr.replace("64", "32")
      elif "128" in instr:
          instr = instr.replace("128", "32")
      elif "256" in instr:
          instr = instr.replace("256", "32")
      # Remove "_e32" or "_e64" from the end of the instruction since we don't care about that yet
      if instr.endswith("_E32") or instr.endswith("_E64"):
          instr = instr[:-4]
      instruction_func = instr
      if instr.startswith("S_"):
          # Scalar instruction, call the right function
          instruction_func = isa.find_instruction_func(instr.upper(), "SCALAR")
      elif instr.startswith("v_"):
          instruction_func = isa.find_instruction_func(instr.upper(), "VECTOR")
      elif instr.startswith("global_"):
          instruction_func = isa.find_instruction_func(instr.upper(), "MEMORY")
      self.fx = instruction_func
  def __repr__(self):
    return f'Instruction[name={self.name} fx={self.fx}]'
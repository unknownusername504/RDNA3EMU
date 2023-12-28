class Operand:
  def __init__(self, type, value):
    self.type = type
    self.value = value
  def __repr__(self) -> str:
    return f'Operand[type={self.type}, value={self.value}]'

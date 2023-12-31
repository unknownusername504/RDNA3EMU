
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AT BINARY BSS COMMA COMMENT DATA DBLCOLON DECIMAL DIRECTIVE EXEC_HI EXEC_LO FLOATING GLOBAL HASH HEX INSTRUCTION INTEGER KERNEL_DESC LABEL LDS_GLOBAL LPAREN MINUS NULL OCTAL OR P2ALIGN PLUS REF RPAREN SET SGPR STRING SYMBOL TARGET TEXT TYPE VCC_HI VCC_LO VGPR WEAKprogram : statementsstatements : statement\n    | statements statementstatement : INSTRUCTION\n    | INSTRUCTION operands\n    | INSTRUCTION operands DBLCOLON INSTRUCTION operands\n    operands : operand\n    | operands COMMA operand\n    | operands operandoperand : SGPR\n    | VGPR\n    | OR VGPR OR\n    | FLOATING\n    | DECIMAL\n    | SYMBOL\n    | BINARY\n    | HEX\n    | EXEC_LO\n    | EXEC_HI\n    | VCC_LO\n    | VCC_HI\n    | OCTAL\n    | NULL\n    | MINUS operand\n    | func\n    | OR func \n    | modifiermodifier : LABEL DECIMALfunc : SYMBOL LPAREN SYMBOL RPAREN\n    | SYMBOL LPAREN DECIMAL RPAREN\n    | SYMBOL LPAREN OCTAL RPAREN\n    | SYMBOL LPAREN FLOATING RPAREN\n    | SYMBOL LPAREN HEX RPAREN'
    
_lr_action_items = {'INSTRUCTION':([0,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,23,24,26,28,30,33,34,36,37,43,44,45,46,47,48,],[4,4,-2,-4,-3,-5,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-25,-27,35,-9,-26,-24,-28,-8,-12,-6,-29,-30,-31,-32,-33,]),'$end':([1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,23,24,28,30,33,34,36,37,43,44,45,46,47,48,],[0,-1,-2,-4,-3,-5,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-25,-27,-9,-26,-24,-28,-8,-12,-6,-29,-30,-31,-32,-33,]),'SGPR':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,33,34,35,36,37,43,44,45,46,47,48,],[8,8,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,8,-25,-27,8,-9,-26,-24,-28,8,-8,-12,8,-29,-30,-31,-32,-33,]),'VGPR':([4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,33,34,35,36,37,43,44,45,46,47,48,],[9,9,-7,-10,-11,29,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,9,-25,-27,9,-9,-26,-24,-28,9,-8,-12,9,-29,-30,-31,-32,-33,]),'OR':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,29,30,33,34,35,36,37,43,44,45,46,47,48,],[10,10,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,10,-25,-27,10,-9,37,-26,-24,-28,10,-8,-12,10,-29,-30,-31,-32,-33,]),'FLOATING':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,32,33,34,35,36,37,43,44,45,46,47,48,],[11,11,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,11,-25,-27,11,-9,-26,41,-24,-28,11,-8,-12,11,-29,-30,-31,-32,-33,]),'DECIMAL':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,30,32,33,34,35,36,37,43,44,45,46,47,48,],[12,12,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,12,-25,-27,34,12,-9,-26,39,-24,-28,12,-8,-12,12,-29,-30,-31,-32,-33,]),'SYMBOL':([4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,32,33,34,35,36,37,43,44,45,46,47,48,],[13,13,-7,-10,-11,31,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,13,-25,-27,13,-9,-26,38,-24,-28,13,-8,-12,13,-29,-30,-31,-32,-33,]),'BINARY':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,33,34,35,36,37,43,44,45,46,47,48,],[14,14,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,14,-25,-27,14,-9,-26,-24,-28,14,-8,-12,14,-29,-30,-31,-32,-33,]),'HEX':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,32,33,34,35,36,37,43,44,45,46,47,48,],[15,15,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,15,-25,-27,15,-9,-26,42,-24,-28,15,-8,-12,15,-29,-30,-31,-32,-33,]),'EXEC_LO':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,33,34,35,36,37,43,44,45,46,47,48,],[16,16,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,16,-25,-27,16,-9,-26,-24,-28,16,-8,-12,16,-29,-30,-31,-32,-33,]),'EXEC_HI':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,33,34,35,36,37,43,44,45,46,47,48,],[17,17,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,17,-25,-27,17,-9,-26,-24,-28,17,-8,-12,17,-29,-30,-31,-32,-33,]),'VCC_LO':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,33,34,35,36,37,43,44,45,46,47,48,],[18,18,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,18,-25,-27,18,-9,-26,-24,-28,18,-8,-12,18,-29,-30,-31,-32,-33,]),'VCC_HI':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,33,34,35,36,37,43,44,45,46,47,48,],[19,19,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,19,-25,-27,19,-9,-26,-24,-28,19,-8,-12,19,-29,-30,-31,-32,-33,]),'OCTAL':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,32,33,34,35,36,37,43,44,45,46,47,48,],[20,20,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,20,-25,-27,20,-9,-26,40,-24,-28,20,-8,-12,20,-29,-30,-31,-32,-33,]),'NULL':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,33,34,35,36,37,43,44,45,46,47,48,],[21,21,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,21,-25,-27,21,-9,-26,-24,-28,21,-8,-12,21,-29,-30,-31,-32,-33,]),'MINUS':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,33,34,35,36,37,43,44,45,46,47,48,],[22,22,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,22,-25,-27,22,-9,-26,-24,-28,22,-8,-12,22,-29,-30,-31,-32,-33,]),'LABEL':([4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,30,33,34,35,36,37,43,44,45,46,47,48,],[25,25,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,25,-25,-27,25,-9,-26,-24,-28,25,-8,-12,25,-29,-30,-31,-32,-33,]),'DBLCOLON':([6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,23,24,28,30,33,34,36,37,44,45,46,47,48,],[26,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-25,-27,-9,-26,-24,-28,-8,-12,-29,-30,-31,-32,-33,]),'COMMA':([6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,23,24,28,30,33,34,36,37,43,44,45,46,47,48,],[27,-7,-10,-11,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-25,-27,-9,-26,-24,-28,-8,-12,27,-29,-30,-31,-32,-33,]),'LPAREN':([13,31,],[32,32,]),'RPAREN':([38,39,40,41,42,],[44,45,46,47,48,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,],[2,]),'statement':([0,2,],[3,5,]),'operands':([4,35,],[6,43,]),'operand':([4,6,22,27,35,43,],[7,28,33,36,7,28,]),'func':([4,6,10,22,27,35,43,],[23,23,30,23,23,23,23,]),'modifier':([4,6,22,27,35,43,],[24,24,24,24,24,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','yacc.py',8),
  ('statements -> statement','statements',1,'p_statements','yacc.py',13),
  ('statements -> statements statement','statements',2,'p_statements','yacc.py',14),
  ('statement -> INSTRUCTION','statement',1,'p_statement','yacc.py',22),
  ('statement -> INSTRUCTION operands','statement',2,'p_statement','yacc.py',23),
  ('statement -> INSTRUCTION operands DBLCOLON INSTRUCTION operands','statement',5,'p_statement','yacc.py',24),
  ('operands -> operand','operands',1,'p_operands','yacc.py',33),
  ('operands -> operands COMMA operand','operands',3,'p_operands','yacc.py',34),
  ('operands -> operands operand','operands',2,'p_operands','yacc.py',35),
  ('operand -> SGPR','operand',1,'p_operand','yacc.py',45),
  ('operand -> VGPR','operand',1,'p_operand','yacc.py',46),
  ('operand -> OR VGPR OR','operand',3,'p_operand','yacc.py',47),
  ('operand -> FLOATING','operand',1,'p_operand','yacc.py',48),
  ('operand -> DECIMAL','operand',1,'p_operand','yacc.py',49),
  ('operand -> SYMBOL','operand',1,'p_operand','yacc.py',50),
  ('operand -> BINARY','operand',1,'p_operand','yacc.py',51),
  ('operand -> HEX','operand',1,'p_operand','yacc.py',52),
  ('operand -> EXEC_LO','operand',1,'p_operand','yacc.py',53),
  ('operand -> EXEC_HI','operand',1,'p_operand','yacc.py',54),
  ('operand -> VCC_LO','operand',1,'p_operand','yacc.py',55),
  ('operand -> VCC_HI','operand',1,'p_operand','yacc.py',56),
  ('operand -> OCTAL','operand',1,'p_operand','yacc.py',57),
  ('operand -> NULL','operand',1,'p_operand','yacc.py',58),
  ('operand -> MINUS operand','operand',2,'p_operand','yacc.py',59),
  ('operand -> func','operand',1,'p_operand','yacc.py',60),
  ('operand -> OR func','operand',2,'p_operand','yacc.py',61),
  ('operand -> modifier','operand',1,'p_operand','yacc.py',62),
  ('modifier -> LABEL DECIMAL','modifier',2,'p_modifier','yacc.py',73),
  ('func -> SYMBOL LPAREN SYMBOL RPAREN','func',4,'p_func','yacc.py',78),
  ('func -> SYMBOL LPAREN DECIMAL RPAREN','func',4,'p_func','yacc.py',79),
  ('func -> SYMBOL LPAREN OCTAL RPAREN','func',4,'p_func','yacc.py',80),
  ('func -> SYMBOL LPAREN FLOATING RPAREN','func',4,'p_func','yacc.py',81),
  ('func -> SYMBOL LPAREN HEX RPAREN','func',4,'p_func','yacc.py',82),
]

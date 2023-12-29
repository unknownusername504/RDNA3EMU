
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AT BINARY BSS COMMA COMMENT DATA DBLCOLON DECIMAL DIRECTIVE FLOATING GLOBAL HASH HEX INSTRUCTION INTEGER KERNEL_DESC LABEL LDS_GLOBAL LPAREN M0 MINUS OCTAL OR P2ALIGN PLUS REF RPAREN SET SGPR STRING SYMBOL TARGET TEXT TYPE VCC_HI VCC_LO VGPR WEAKprogram : statementsstatements : statement\n                  | statements statementstatement : INSTRUCTION\n                 | INSTRUCTION operands\n                 | INSTRUCTION operands DBLCOLON INSTRUCTION operands\n    operands : operand\n                | operands COMMA operand\n                | operands OR operand\n                | operands operandoperand : SGPR \n               | VGPR \n               | FLOATING\n               | DECIMAL\n               | SYMBOL\n               | BINARY\n               | HEX\n               | OCTAL\n               | func\n               | modifiermodifier : LABEL DECIMAL func : SYMBOL LPAREN SYMBOL RPAREN\n           | SYMBOL LPAREN DECIMAL RPAREN\n           | SYMBOL LPAREN OCTAL RPAREN\n           | SYMBOL LPAREN FLOATING RPAREN\n           | SYMBOL LPAREN HEX RPAREN'
    
_lr_action_items = {'INSTRUCTION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,24,26,27,33,34,35,36,37,38,],[4,4,-2,-4,-3,-5,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,25,-10,-21,-8,-9,-6,-22,-23,-24,-25,-26,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,21,24,26,27,33,34,35,36,37,38,],[0,-1,-2,-4,-3,-5,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-10,-21,-8,-9,-6,-22,-23,-24,-25,-26,]),'SGPR':([4,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,24,25,26,27,33,34,35,36,37,38,],[8,8,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,8,-10,8,-21,8,-8,-9,8,-22,-23,-24,-25,-26,]),'VGPR':([4,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,24,25,26,27,33,34,35,36,37,38,],[9,9,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,9,-10,9,-21,9,-8,-9,9,-22,-23,-24,-25,-26,]),'FLOATING':([4,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,33,34,35,36,37,38,],[10,10,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,10,-10,10,31,-21,10,-8,-9,10,-22,-23,-24,-25,-26,]),'DECIMAL':([4,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,25,26,27,33,34,35,36,37,38,],[11,11,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,24,11,-10,11,29,-21,11,-8,-9,11,-22,-23,-24,-25,-26,]),'SYMBOL':([4,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,33,34,35,36,37,38,],[12,12,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,12,-10,12,28,-21,12,-8,-9,12,-22,-23,-24,-25,-26,]),'BINARY':([4,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,24,25,26,27,33,34,35,36,37,38,],[13,13,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,13,-10,13,-21,13,-8,-9,13,-22,-23,-24,-25,-26,]),'HEX':([4,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,33,34,35,36,37,38,],[14,14,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,14,-10,14,32,-21,14,-8,-9,14,-22,-23,-24,-25,-26,]),'OCTAL':([4,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,33,34,35,36,37,38,],[15,15,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,15,-10,15,30,-21,15,-8,-9,15,-22,-23,-24,-25,-26,]),'LABEL':([4,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,24,25,26,27,33,34,35,36,37,38,],[18,18,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,18,-10,18,-21,18,-8,-9,18,-22,-23,-24,-25,-26,]),'DBLCOLON':([6,7,8,9,10,11,12,13,14,15,16,17,21,24,26,27,34,35,36,37,38,],[19,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-10,-21,-8,-9,-22,-23,-24,-25,-26,]),'COMMA':([6,7,8,9,10,11,12,13,14,15,16,17,21,24,26,27,33,34,35,36,37,38,],[20,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-10,-21,-8,-9,20,-22,-23,-24,-25,-26,]),'OR':([6,7,8,9,10,11,12,13,14,15,16,17,21,24,26,27,33,34,35,36,37,38,],[22,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-10,-21,-8,-9,22,-22,-23,-24,-25,-26,]),'LPAREN':([12,],[23,]),'RPAREN':([28,29,30,31,32,],[34,35,36,37,38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,],[2,]),'statement':([0,2,],[3,5,]),'operands':([4,25,],[6,33,]),'operand':([4,6,20,22,25,33,],[7,21,26,27,7,21,]),'func':([4,6,20,22,25,33,],[16,16,16,16,16,16,]),'modifier':([4,6,20,22,25,33,],[17,17,17,17,17,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','yacc.py',9),
  ('statements -> statement','statements',1,'p_statements','yacc.py',13),
  ('statements -> statements statement','statements',2,'p_statements','yacc.py',14),
  ('statement -> INSTRUCTION','statement',1,'p_statement','yacc.py',21),
  ('statement -> INSTRUCTION operands','statement',2,'p_statement','yacc.py',22),
  ('statement -> INSTRUCTION operands DBLCOLON INSTRUCTION operands','statement',5,'p_statement','yacc.py',23),
  ('operands -> operand','operands',1,'p_operands','yacc.py',37),
  ('operands -> operands COMMA operand','operands',3,'p_operands','yacc.py',38),
  ('operands -> operands OR operand','operands',3,'p_operands','yacc.py',39),
  ('operands -> operands operand','operands',2,'p_operands','yacc.py',40),
  ('operand -> SGPR','operand',1,'p_operand','yacc.py',49),
  ('operand -> VGPR','operand',1,'p_operand','yacc.py',50),
  ('operand -> FLOATING','operand',1,'p_operand','yacc.py',51),
  ('operand -> DECIMAL','operand',1,'p_operand','yacc.py',52),
  ('operand -> SYMBOL','operand',1,'p_operand','yacc.py',53),
  ('operand -> BINARY','operand',1,'p_operand','yacc.py',54),
  ('operand -> HEX','operand',1,'p_operand','yacc.py',55),
  ('operand -> OCTAL','operand',1,'p_operand','yacc.py',56),
  ('operand -> func','operand',1,'p_operand','yacc.py',57),
  ('operand -> modifier','operand',1,'p_operand','yacc.py',58),
  ('modifier -> LABEL DECIMAL','modifier',2,'p_modifier','yacc.py',62),
  ('func -> SYMBOL LPAREN SYMBOL RPAREN','func',4,'p_func','yacc.py',66),
  ('func -> SYMBOL LPAREN DECIMAL RPAREN','func',4,'p_func','yacc.py',67),
  ('func -> SYMBOL LPAREN OCTAL RPAREN','func',4,'p_func','yacc.py',68),
  ('func -> SYMBOL LPAREN FLOATING RPAREN','func',4,'p_func','yacc.py',69),
  ('func -> SYMBOL LPAREN HEX RPAREN','func',4,'p_func','yacc.py',70),
]

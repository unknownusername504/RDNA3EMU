# This file defines the instruction set for RNDA3.
import sys

# Add rdna3emu to path
sys.path.append("../rdna3emu/")

import ply.lex as lex
from rdna3emu.isa.instruction_set import InstructionSet
# CAUSING CIRCULAR IMPORT WITH PARSER.PY
# from rdna3emu.parser.lex import Lexer


class AsmInterpreter:
    def __init__(self):
        self.lexer = Lexer().get_lex()
        self.isa = InstructionSet()
        self.clause_code_block = []
        # The clause length is: (SIMM16[5:0] + 1)
        self.clause_simm16 = 0
        self.clause_code_block_length = 0

    def make_token(self, type, value, lineno, lexpos):
        token = lex.LexToken()
        token.type = type
        token.value = value
        token.lineno = lineno
        token.lexpos = lexpos
        return token

    # Pre-Process an op token
    def preprocess_op_token(self, token):
        # Convert to uppercase string
        token_str = token.value.upper()
        # The register array parsing will mean we should treat anything higher than 1 dword as 1 dword ops
        # so we can just set the size part of the instruction to 32
        if "64" in token_str:
            token_str = token_str.replace("64", "32")
        elif "128" in token_str:
            token_str = token_str.replace("128", "32")
        elif "256" in token_str:
            token_str = token_str.replace("256", "32")
        # Remove "_e32" or "_e64" from the end of the instruction since we don't care about that yet
        if token_str.endswith("_E32") or token_str.endswith("_E64"):
            token_str = token_str[:-4]
        return self.make_token(token.type, token_str, token.lineno, token.lexpos)

    # Pre-Process a register token
    def preprocess_register_token(self, token):
        tokens = []
        token_str = str(token.value)
        # Expand registers with array format [x:y] to individual registers
        if "[" in token_str:
            # Get the register range
            register_range = token_str.split("[")[1][:-1]
            # Get the start and end of the range
            start, end = register_range.split(":")
            # Convert to integers
            start = int(start)
            end = int(end)
            # Add the registers to the tokens list
            for i in range(start, end + 1):
                tokens.append(
                    self.make_token(token.type, int(i), token.lineno, token.lexpos)
                )
        else:
            tokens.append(token)
        return tokens

    # Check if a token is a valid hex integer
    def is_valid_hex(self, token):
        if not token.startswith("0x"):
            return False
        # Check that the integer is valid
        try:
            int(token, 16)
        except ValueError:
            return False
        return True

    # Check if a token is a valid decimal integer
    def is_valid_decimal(self, token):
        # Check that the integer is valid
        try:
            int(token)
        except ValueError:
            return False
        return True

    # Pre-Process an integer token
    def preprocess_integer_token(self, token):
        # Return if the token is already an integer
        if isinstance(token.value, int):
            return token
        # LexToken(INTEGER,'0x...',...)
        if "0x" in token.value:
            # Check that the integer is valid
            if not self.is_valid_hex(token.value):
                raise Exception("Invalid hex integer")
            return self.make_token(
                token.type, int(token.value, 16), token.lineno, token.lexpos
            )
        else:
            raise Exception("Invalid integer")

    # Check if a token is a valid floating point number
    def is_valid_floating(self, token):
        # Check that the integer is valid
        try:
            float(token.value)
        except ValueError:
            return False
        return True

    # Pre-Process a floating point token
    def preprocess_floating_token(self, token):
        # LexToken(FLOATING,'...',...)
        if "." in token.value:
            # Check that the float is valid
            if not self.is_valid_floating(token):
                raise Exception("Invalid floating point number")
            return self.make_token(
                token.type, float(token.value), token.lineno, token.lexpos
            )
        else:
            raise Exception("Invalid floating point number")

    # Execute an instruction
    def process_instruction(self, tokens):
        # Preprocess the token
        op_token = self.preprocess_op_token(tokens[0])
        # Preprocess the register tokents if they are VGPR or SGPR
        for i in range(1, len(tokens)):
            if tokens[i].type == "VGPR" or tokens[i].type == "SGPR":
                reg_tokens = self.preprocess_register_token(tokens[i])
                # Replicate this entire instruction for each register if the register is an array
                if len(reg_tokens) > 1:
                    for reg_token in reg_tokens:
                        tokens[i] = reg_token
                        self.process_instruction(tokens)
            # Process the symbol tokens
            elif tokens[i].type == "SYMBOL":
                # We can handle global_load and global_store here so don't preprocess them
                if not (
                    tokens[i].value.startswith("global_load")
                    or tokens[i].value.startswith("global_store")
                ):
                    # Skip symbol tokens that are not global_load or global_store
                    return
            # Process the label tokens
            elif tokens[i].type == "LABEL":
                # We can handle offset labels but not other labels
                if not tokens[i].value.startswith("offset"):
                    # Skip label tokens that are not offset labels
                    return
                # Remove this token and the next token will be the offset as an integer
                tokens = tokens.remove(tokens[i])
            # Preprocess the integer tokens
            elif tokens[i].type == "INTEGER":
                tokens[i] = self.preprocess_integer_token(tokens[i])
            # Preprocess the floating point tokens
            elif tokens[i].type == "FLOATING":
                tokens[i] = self.preprocess_floating_token(tokens[i])
            else:
                raise Exception("Invalid token type")

        instruction_func = None
        # Get the instruction type
        if op_token.value.startswith("S_"):
            # Scalar instruction, call the right function
            instruction_func = self.isa.find_instruction_func(op_token.value, "SCALAR")
        elif op_token.value.startswith("V_"):
            instruction_func = self.isa.find_instruction_func(op_token.value, "VECTOR")
        elif op_token.value.startswith("GLOBAL_"):
            instruction_func = self.isa.find_instruction_func(op_token.value, "MEMORY")

        # Check if the instruction is s_clause
        if op_token.value == "S_CLAUSE":
            # Start accumulating the clause code block
            self.clause_code_block = []
            self.clause_simm16 = int(tokens[1].value)
            self.clause_code_block_length = (self.clause_simm16 & 0x3F) + 1
            return

        # Check that there was enough code to populate the clause code block
        if (op_token.value == "S_ENDPGM") and (self.clause_code_block_length > 0):
            raise Exception("Invalid clause code block length")

        if instruction_func is not None:
            # Remove the instruction token
            tokens = tokens[1:]
            print(tokens)
            # Get the values of the tokens if they are LexTokens
            for i in range(len(tokens)):
                if isinstance(tokens[i], lex.LexToken):
                    tokens[i] = tokens[i].value
            print(tokens)
            # Call the instruction function
            # Check that we have the right number of tokens
            if len(tokens) != instruction_func.__code__.co_argcount - 1:
                raise Exception(
                    f"Wrong number of arguments for instruction {op_token} (expected {instruction_func.__code__.co_argcount - 1}, got {len(tokens)})"
                )
        else:
            raise Exception(f"Instruction {op_token} not implemented")

        if self.clause_code_block_length > 0:
            clause_code_block_pair = (instruction_func, tokens)
            self.clause_code_block.append(clause_code_block_pair)
            self.clause_code_block_length -= 1
            # Return if we have not reached the end of the clause code block
            if self.clause_code_block_length > 0:
                return

        if (self.clause_code_block_length == 0) and (len(self.clause_code_block) > 0):
            # Process the clause code block
            # Call the s_clause instruction function
            instruction_func = self.isa.find_instruction_func("S_CLAUSE", "SCALAR")
            instruction_func(self.clause_simm16, self.clause_code_block)
            # Reset the clause code block
            self.clause_code_block = []
            self.clause_simm16 = 0
            self.clause_code_block_length = 0
        else:
            instruction_func(*tokens)

    def interpret_asm(self):
        tokens = []
        # Tokenize
        while True:
            token = self.lexer.token()
            if not token:
                # Process the tokens for the last instruction
                print(tokens)
                self.process_instruction(tokens)
                break  # No more input
            print(token)
            if token.type == "INSTRUCTION":
                # Do not perform this step if it is the first instruction
                if len(tokens) > 0:
                    # Process the tokens for the previous instruction
                    print(tokens)
                    self.process_instruction(tokens)
                    tokens = []
            elif token.type not in [
                "VGPR",
                "SGPR",
                "SYMBOL",
                "LABEL",
                "INTEGER",
                "FLOATING",
            ]:
                # Discard anything other than "INSTRUCTION", "VGPR", "SGPR", "SYMBOL", "LABEL", "INTEGER", "FLOATING"
                continue

            tokens.append(token)


def run():
    asm_interpreter = AsmInterpreter()
    asm_interpreter.interpret_asm()


if __name__ == "__main__":
    run()

# This file defines the instruction set for RNDA3.
import sys

# Add rdna3emu to path
sys.path.append("../rdna3emu/")

import ply.lex as lex
from rdna3emu.isa.instruction_set import InstructionSet

from rdna3emu.parser.legacy_lex import Lexer

# Declare type for register ids that is an int but won't be confused with other ints when using isinstance
RegisterId = int


class AsmInterpreter:
    def __init__(self):
        self.lexer = Lexer("Data\\tinyconvdump.txt").get_lex()
        self.isa = InstructionSet()
        self.clause_code_block = []
        # The clause length is: (SIMM16[5:0] + 1)
        self.clause_simm16 = 0
        self.clause_code_block_length = 0
        self.instruction_count = 1

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
                tokens.append(
                    self.make_token(
                        token.type, register_name + str(i), token.lineno, token.lexpos
                    )
                )
        else:
            # Remove leading "v" or "s" if it exists
            if token_str.startswith("v") or token_str.startswith("s"):
                token_str = token_str[1:]
            tokens.append(
                self.make_token(
                    token.type, RegisterId(token_str), token.lineno, token.lexpos
                )
            )
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
            print("Hex integer detected for token {}".format(token))
            new_token = self.make_token(
                token.type, int(token.value, 16), token.lineno, token.lexpos
            )
            print("New token {}".format(new_token))
            return new_token
        elif isinstance(token.value, str):
            # Check that the integer is valid
            if not self.is_valid_decimal(token.value):
                raise Exception("Invalid decimal integer")
            print("Decimal integer detected for token {}".format(token))
            new_token = self.make_token(
                token.type, int(token.value), token.lineno, token.lexpos
            )
            print("New token {}".format(new_token))
            return new_token
        else:
            raise Exception("Invalid integer", token.value)

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

    def preprocess_global(self, tokens):
        # Split the scalar register array into 2 scalar registers
        # The first register is the lower 32 bits and the second register is the upper 32 bits
        # Find the register array
        for i in range(1, len(tokens)):
            if tokens[i].type == "SGPR":
                reg_tokens = self.preprocess_register_token(tokens[i])
                # Check that the register is an array
                if len(reg_tokens) == 2:
                    reg_token_s0 = self.preprocess_register_token(reg_tokens[0])[0]
                    reg_token_s1 = self.preprocess_register_token(reg_tokens[1])[0]
                    # Prepend the second register to the tokens list
                    tokens = tokens[:i] + [reg_token_s1] + tokens[i:]
                    # Replace the first register with the first 32 bits of the second register
                    tokens[i] = reg_token_s0
                    break
                else:
                    # Probably already processed so just return
                    break
        return tokens

    # Execute an instruction
    def process_instruction(self, tokens):
        # Preprocess the token
        op_token = self.preprocess_op_token(tokens[0])
        # Preprocess the global_* instructions
        if op_token.value.startswith("GLOBAL_"):
            tokens = self.preprocess_global(tokens)
        for i in range(len(tokens)):
            # Remove the offset label tokens
            if tokens[i].type == "LABEL":
                if tokens[i].value.startswith("offset"):
                    # Remove this token and the next token will be the offset as an integer
                    tokens = tokens[:i] + tokens[i + 1 :]
                    break

        # Preprocess the register tokents if they are VGPR or SGPR
        for i in range(1, len(tokens)):
            if tokens[i].type == "VGPR" or tokens[i].type == "SGPR":
                reg_tokens = self.preprocess_register_token(tokens[i])
                # Replicate the instruction for each register
                if len(reg_tokens) > 1:
                    for reg_token in reg_tokens:
                        tokens[i] = reg_token
                        self.process_instruction(tokens)
                    return
                else:
                    tokens[i] = reg_tokens[0]
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
                    return
            # Preprocess the integer tokens
            elif tokens[i].type == "INTEGER":
                tokens[i] = self.preprocess_integer_token(tokens[i])
            # Preprocess the floating point tokens
            elif tokens[i].type == "FLOATING":
                tokens[i] = self.preprocess_floating_token(tokens[i])
            else:
                raise Exception("Invalid token type")

        print("Instruction {} : {}".format(self.instruction_count, tokens))
        self.instruction_count += 1

        instruction_func = None
        # Get the instruction type
        if op_token.value.startswith("S_"):
            # Scalar instruction, call the right function
            instruction_func = self.isa.find_instruction_func(op_token.value, "SCALAR")
        elif op_token.value.startswith("V_"):
            instruction_func = self.isa.find_instruction_func(op_token.value, "VECTOR")
        elif op_token.value.startswith("GLOBAL_"):
            instruction_func = self.isa.find_instruction_func(op_token.value, "MEMORY")
        elif op_token.value.startswith("DS_"):
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
            # Get the values of the tokens if they are LexTokens
            for i in range(len(tokens)):
                if isinstance(tokens[i], lex.LexToken):
                    tokens[i] = tokens[i].value
            # Call the instruction function
            # Check that we have the right number of tokens
            num_optional_args = (
                len(instruction_func.__defaults__)
                if instruction_func.__defaults__
                else 0
            )
            if (
                len(tokens) + num_optional_args
            ) == instruction_func.__code__.co_argcount - 1:
                # Add the optional arguments to the end of the tokens list
                # Probably not scalable when only some of the optional arguments are used
                for i in range(num_optional_args):
                    tokens.append(instruction_func.__defaults__[i])
            if len(tokens) != instruction_func.__code__.co_argcount - 1:
                raise Exception(
                    f"Wrong number of arguments for instruction {op_token} (expected at least {instruction_func.__code__.co_argcount - 1 - num_optional_args}, got {len(tokens)})"
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
                self.process_instruction(tokens)
                break  # No more input
            if token.type == "INSTRUCTION":
                # Do not perform this step if it is the first instruction
                if len(tokens) > 0:
                    # Process the tokens for the previous instruction
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
    asm_interpreter.isa.dump_registers()
    asm_interpreter.isa.dump_memory()


if __name__ == "__main__":
    run()

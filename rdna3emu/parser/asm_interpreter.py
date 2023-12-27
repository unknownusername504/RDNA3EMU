import ply.lex as lex
from rdna3emu.isa.instruction_set import InstructionSet


class AsmInterpreter:
    def __init__(self):
        self.lexer = lex.lex()
        self.asm_code = self.get_asm_code()
        self.lexer.input(self.asm_code)
        self.instruction_type_prefixes = ["S_", "V_"]
        self.isa = InstructionSet()

    # Interpret the RDNA3 ISA assembly code generated by the compiler (HIP)
    def get_asm_code(self):
        with open("../../Data/example_asm.asm", "r") as f:
            data = f.read()
            return data

    # Pre-Process an op token
    def preprocess_op_token(self, token):
        # Convert to uppercase
        token = token.upper()
        # Remove "_e32" or "_e64" from the end of the instruction
        if token.endswith("_E32") or token.endswith("_E64"):
            token = token[:-4]
        return token

    # PRe-Process a register token
    def preprocess_register_token(self, token):
        tokens = []
        # Expand registers with array format [x:y] to individual registers
        if "[" in token.value:
            # Get the register name
            register_name = token.value.split("[")[0]
            # Get the register range
            register_range = token.value.split("[")[1][:-1]
            # Get the start and end of the range
            start, end = register_range.split(":")
            # Convert to integers
            start = int(start)
            end = int(end)
            # Add the registers to the tokens list
            for i in range(start, end + 1):
                tokens.append(lex.LexToken(token.type, register_name + str(i)))
        else:
            tokens.append(token)
        return tokens

    # Pre-Process a symbol token
    def preprocess_symbol_token(self, token):
        # Tokens are special symbols that need to be handled differently
        # LexToken(SYMBOL,'exec',...)
        if token.value == "exec":
            self.process_exec()
        # LexToken(SYMBOL,'global_load_b64',...)
        elif token.value.contains("global_load"):
            global_load_type = token.value.split("_")[-1]
            self.process_global_load(global_load_type)
        # LexToken(SYMBOL,'vmcnt',...)
        elif token.value == "vmcnt":
            self.process_vmcnt()
        else:
            raise Exception("Invalid symbol")

    # Pre-Process a label token
    def preprocess_label_token(self, token):
        # LexToken(LABEL,'offset:',...)
        if token.value.contains("offset"):
            # Strip the colon
            self.process_label(token.value[:-1])
        else:
            raise Exception("Invalid label")

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
        # LexToken(INTEGER,'0x...',...)
        if token.value.contains("0x"):
            # Check that the integer is valid
            if not self.is_valid_hex(token.value):
                raise Exception("Invalid hex integer")
            self.process_integer(token.value)
        # LexToken(INTEGER,'...',...)
        elif token.value == "0":
            # Check that the integer is valid
            if not self.is_valid_decimal(token.value):
                raise Exception("Invalid decimal integer")
            self.process_integer(token.value)
        else:
            raise Exception("Invalid integer")

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
                        tokens[i] = lex.LexToken(tokens[i].type, reg_token)
                        self.process_instruction(tokens)
        instruction_types = self.isa.get_instruction_types()
        instruction_func = None
        # Get the instruction type
        if op_token.startswith("S_"):
            # Scalar instruction, call the right function
            instruction_func = self.isa.get_instruction_func(
                op_token, instruction_types["SCALAR"]
            )
        elif op_token.startswith("V_"):
            instruction_func = self.isa.get_instruction_func(
                op_token, instruction_types["VECTOR"]
            )

        if instruction_func is not None:
            # Remove the instruction token
            tokens = tokens[1:]
            # Call the instruction function
            # Check that we have the right number of tokens
            if len(tokens) != instruction_func.__code__.co_argcount:
                raise Exception(
                    f"Wrong number of arguments for instruction {op_token} (expected {instruction_func.__code__.co_argcount}, got {len(tokens)})"
                )
            # Remove the instruction token
            instruction_func(tokens)
        else:
            raise Exception(f"Instruction {op_token} not implemented")

    def interpret_asm(self):
        tokens = []
        # Tokenize
        while True:
            token = self.lexer.token()
            if not token:
                break  # No more input
            print(token)
            if token.type == "INSTRUCTION":
                # Process the tokens for the previous instruction
                self.process_instruction(tokens)
                tokens = []
            elif token.type not in ["VGPR", "SGPR", "SYMBOL", "LABEL", "INTEGER"]:
                # Discard anything other than "INSTRUCTION", "VGPR", "SGPR", "SYMBOL", "LABEL", "INTEGER"
                continue

            tokens.append(token)


def run():
    asm_interpreter = AsmInterpreter()
    asm_interpreter.interpret_asm()


if __name__ == "__main__":
    run()

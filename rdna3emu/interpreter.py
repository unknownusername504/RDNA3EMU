from rdna3emu.parser.ir import Instruction, isa
from rdna3emu.isa.registers import VectorRegister, ScalarRegister


def build_executable(stmts):
    exec = []
    clause = None
    i = 0
    while i < len(stmts):
        stmt = stmts[i]
        if isinstance(stmt, list):
            instr = stmt[0]
            operands = stmt[1:]
            if instr.name.startswith("V_DUAL"):
                next_operands = []
                for j, oper in enumerate(operands):
                    if isinstance(oper, Instruction):
                        exec.append(extract_exec(instr, next_operands))
                        exec.append(extract_exec(oper, operands[j + 1 :]))
                        break
                    else:
                        next_operands.append(oper)
            else:
                r = extract_exec(instr, operands)
                if r:
                    exec.append(r)
            i += 1
        else:
            exec.append(stmt.fx)
            i += 1
    return exec


ignore_instr = {"S_DELAY_ALU", "S_WAITCNT", "S_SENDMSG", "S_CLAUSE"}


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
                    for reg in sub_operand.registers:
                        # Add the register to the tokens list as an int (without the 's' or 'v') and subtype it as a register
                        reg_type = reg[0]
                        reg_value = int(reg[1:])
                        if reg_type == "s":
                            args.append(ScalarRegister(reg_value))
                        elif reg_type == "v":
                            args.append(VectorRegister(reg_value))
                else:
                    args.append(sub_operand.value)
        else:
            if operand.registers:
                for reg in operand.registers:
                    args.append(int(reg[1:]))
            else:
                args.append(operand.value)

    return (instr.fx, args)


def get_isa():
    return isa


def run(executable, print_instr=True, dump=True):
    for instr in executable:
        try:
            # s_endpgm and s_code_end are the only instructions that don't take any arguments and are not arrays but are callable methods
            # Check that instr is a method and not a tuple
            if callable(instr):
                instr = (instr, [])
            # v_cndmask_b32 isn't parsing the last argument correctly which is vcc_lo so we need to add it manually
            if instr[0] == isa.vector_ops.v_cndmask_b32:
                if len(instr[1]) == 3:
                    instr[1].append("vcc_lo")
            instr[0](*instr[1])
            if print_instr:
                print(instr[0], instr[1])
        except Exception as e:
            # Re-raise the exception with the instruction appended
            e.args = e.args + (instr,)
            raise e
    if dump:
        isa.dump_memory(non_zero=True)
        isa.dump_registers(non_zero=True, print_all=False)

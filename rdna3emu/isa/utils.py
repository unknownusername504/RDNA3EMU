import numpy as np
import os


def rev_b32(x):
    # Bitmask constants for reversing bits in a 32-bit integer
    mask1 = 0x55555555  # 01010101010101010101010101010101
    mask2 = 0x33333333  # 00110011001100110011001100110011
    mask4 = 0x0F0F0F0F  # 00001111000011110000111100001111
    mask8 = 0x00FF00FF  # 00000000111111110000000011111111

    x = ((x >> 1) & mask1) | ((x & mask1) << 1)
    x = ((x >> 2) & mask2) | ((x & mask2) << 2)
    x = ((x >> 4) & mask4) | ((x & mask4) << 4)
    x = ((x >> 8) & mask8) | ((x & mask8) << 8)
    x = (x >> 16) | (x << 16)

    return x


def rev_b64(x):
    # Bitmask constants for reversing bits in a 64-bit integer
    mask1 = 0x5555555555555555  # 0101010101010101010101010101010101010101010101010101010101010101
    mask2 = 0x3333333333333333  # 0011001100110011001100110011001100110011001100110011001100110011
    mask4 = 0x0F0F0F0F0F0F0F0F  # 0000111100001111000011110000111100001111000011110000111100001111
    mask8 = 0x00FF00FF00FF00FF  # 0000000011111111000000001111111100000000111111110000000011111111

    x = ((x >> 1) & mask1) | ((x & mask1) << 1)
    x = ((x >> 2) & mask2) | ((x & mask2) << 2)
    x = ((x >> 4) & mask4) | ((x & mask4) << 4)
    x = ((x >> 8) & mask8) | ((x & mask8) << 8)
    x = ((x >> 16) & 0x0000FFFF0000FFFF) | ((x & 0x0000FFFF0000FFFF) << 16)
    x = (x >> 32) | (x << 32)

    return x


def ctz(x, size=32):
    tmp = -1
    for i in range(0, size):
        if x & 1:
            tmp = i
            break
        x >>= 1
    return tmp


def clz(x, size=32):
    tmp = -1
    m = 1 << size
    for i in range(size, -1, -1):
        if x & m:
            tmp = (size - 1) - i
            break
        x <<= 1
    return tmp


def cls(x, size=32):
    tmp = -1
    sign_bit = (x >> (size - 1)) & 1
    for i in range(1, size):
        next_bit = (x & (1 << (size - 2))) >> (size - 2)
        if sign_bit != next_bit:
            tmp = i
            break
        x <<= 1
    return tmp


def count_zero_bits(x, size=32):
    count = 0
    for i in range(size):
        if (x & (1 << i)) == 0:
            count += 1
    return count


def count_one_bits(x, size=32):
    count = 0
    for i in range(size):
        if x & (1 << i):
            count += 1
    return count


def fp16_to_fp32(fp16_val):
    """
    Convert a 16-bit half-precision floating-point number to a 32-bit single-precision floating-point number.

    :param fp16_val: The 16-bit floating-point number to convert.
    :return: A 32-bit single-precision floating-point representation of the input.
    """
    fp16_val = np.float16(fp16_val)

    return np.float32(fp16_val)


def fp32_to_fp16(value):
    value = np.float32(value)

    return np.float16(value)


def sext_i32(x, in_sz=8):
    m = 1 << (in_sz - 1)
    if m & x:
        return x | 0xFFFFFF00
    return x


def bitset0(x, offset):
    return x & (~(1 << offset))


def bitset1(x, offset):
    return x | (1 << offset)


def bitreplicate(x):
    tmp = x
    r = 0
    for i in range(0, 32):
        if tmp & 1:
            r = bitset1(r, i * 2)
            r = bitset1(r, i * 2 + 1)
        else:
            r = bitset0(r, i * 2)
            r = bitset0(r, i * 2 + 1)
        tmp >>= 1
    return r


def bitcnt(x, bit=0, sz=32):
    tmp = 0
    for i in range(0, sz):
        if x & 1 == bit:
            tmp += 1
        x >>= 1
    return tmp


# Function to parse the asm file and output used instructions
def find_used_instructions(asm_file, instructions):
    parsed_instructions = set()
    with open(asm_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            # Trim whitespace
            line = line.strip()
            if line.startswith("s_") or line.startswith("v_"):
                op_token = line.split()[0]
                # Convert to uppercase
                op_token = op_token.upper()
                # Remove "_e32" or "_e64" from the end of the instruction
                if op_token.endswith("_E32") or op_token.endswith("_E64"):
                    op_token = op_token[:-4]
                # Check if the instruction is in the instruction set
                for instruction in instructions:
                    if op_token in instructions[instruction]:
                        parsed_instructions.add(op_token)

    # Go through the instruction set and find the used instructions
    used_instructions = []
    for instruction in instructions:
        for op in instructions[instruction]:
            if op in parsed_instructions:
                used_instructions.append(op)

    # Save used instructions to file
    folder_path = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(folder_path, "instruction_usage")
    save_path = os.path.join(folder_path, "used_instructions.txt")
    with open(save_path, "w") as f:
        for instruction in used_instructions:
            f.write(instruction + "\n")

    return used_instructions


# Function to parse the asm file and output unimplemented instructions
def find_unimplemented_instructions(asm_file, instructions):
    parsed_instructions = set()
    with open(asm_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            # Trim whitespace
            line = line.strip()
            if line.startswith("s_") or line.startswith("v_"):
                op_token = line.split()[0]
                # Convert to uppercase
                op_token = op_token.upper()
                # Remove "_e32" or "_e64" from the end of the instruction
                if op_token.endswith("_E32") or op_token.endswith("_E64"):
                    op_token = op_token[:-4]
                parsed_instructions.add(op_token)

    # Get the used instructions
    used_instructions = find_used_instructions(asm_file, instructions)

    # Remove used instructions from parsed instructions
    for instruction in used_instructions:
        parsed_instructions.remove(instruction)

    # Unimplemented instructions are left in parsed_instructions
    unimplemented_instructions = list(parsed_instructions)

    # Sort the list
    unimplemented_instructions.sort()

    # Save used instructions to file
    folder_path = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(folder_path, "instruction_usage")
    save_path = os.path.join(folder_path, "unimplemented_instructions.txt")
    with open(save_path, "w") as f:
        for instruction in unimplemented_instructions:
            f.write(instruction + "\n")

    return unimplemented_instructions


# Function to parse the asm file and output unused instructions
def find_unused_instructions(asm_file, instructions):
    used_instructions = find_used_instructions(asm_file, instructions)
    unused_instructions = []
    for instruction in instructions:
        for op in instructions[instruction]:
            if op not in used_instructions:
                unused_instructions.append(op)

    # Save unused instructions to file
    folder_path = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(folder_path, "instruction_usage")
    save_path = os.path.join(folder_path, "unused_instructions.txt")
    with open(save_path, "w") as f:
        for instruction in unused_instructions:
            f.write(instruction + "\n")

    return unused_instructions


def populate_instruction_usage(instructions):
    cwd = os.getcwd()
    asm_file = os.path.join(cwd, "Data/example_asm.asm")
    find_used_instructions(asm_file, instructions)
    find_unimplemented_instructions(asm_file, instructions)
    find_unused_instructions(asm_file, instructions)


if __name__ == "__main__":
    print(bitcnt(x, bit=1))
    print(bitcnt(0, bit=1))
    print(bitcnt(0xFFFFFFFF, bit=1))
    print(bitcnt(0xFFFFFFFFFFFFFFFF, bit=1, sz=64))
    print(cls(0, 32))
    print(cls(0x0000CCCC, 32))
    print(cls(0xFFFF3333, 32))
    print(cls(0x7FFFFFFF, 32))
    print(cls(0x80000000, 32))
    print(cls(0xFFFFFFFF, 32))
    x = 0b1100_1011
    print(format(x, "08b"))
    print(format(sext_i32(x), "032b"))
    x = 0b0100_1111
    print(format(sext_i32(x), "032b"))
    x = 0b0100_1111_1111_0000
    print(format(sext_i32(x, 16), "032b"))
    x = 0b1100_1111_1111_0000
    print(format(sext_i32(x, 16), "032b"))
    print(bin(bitset0(0b1111, 3)))
    print(bin(bitset1(0b0000, 3)))
    x = 0b0101_0101_0101_0101_0101_0101_0101_0101
    print(format(bitreplicate(x), "064b"))

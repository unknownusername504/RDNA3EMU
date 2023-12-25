import numpy as np
def rev_b32(x):
    # Bitmask constants for reversing bits in a 32-bit integer
    mask1 = 0x55555555  # 01010101010101010101010101010101
    mask2 = 0x33333333  # 00110011001100110011001100110011
    mask4 = 0x0f0f0f0f  # 00001111000011110000111100001111
    mask8 = 0x00ff00ff  # 00000000111111110000000011111111

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
    mask4 = 0x0f0f0f0f0f0f0f0f  # 0000111100001111000011110000111100001111000011110000111100001111
    mask8 = 0x00ff00ff00ff00ff  # 0000000011111111000000001111111100000000111111110000000011111111

    x = ((x >> 1) & mask1) | ((x & mask1) << 1)
    x = ((x >> 2) & mask2) | ((x & mask2) << 2)
    x = ((x >> 4) & mask4) | ((x & mask4) << 4)
    x = ((x >> 8) & mask8) | ((x & mask8) << 8)
    x = ((x >> 16) & 0x0000FFFF0000FFFF) | ((x & 0x0000FFFF0000FFFF) << 16)
    x = (x >> 32) | (x << 32)
    
    return x

def ctz(x, size=32):
    tmp = -1
    for i in range(0,size):
        if x & 1:
            tmp = i
            break
        x >>= 1
    return tmp


def clz(x, size=32):
    tmp = -1
    m = 1 << size
    for i in range(size,-1,-1):
        if x & m:
            tmp = (size-1) - i 
            break
        x <<= 1
    return tmp 

def cls(x, size=32):
    tmp = -1
    sign_bit = (x>>(size-1)) & 1 
    for i in range(1, size):
        next_bit = (x & (1<<(size-2))) >> (size-2)
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


print(cls(0, 32))
print(cls(0x0000cccc, 32))
print(cls(0xffff3333, 32))
print(cls(0x7fffffff, 32))
print(cls(0x80000000, 32))
print(cls(0xffffffff, 32))

def sext_i32(x, in_sz=8):
    m = 1 << (in_sz-1)
    if m & x:
        return x | 0xFFFFFF00
    return x

x = 0b1100_1011
print(format(x, '08b'))
print(format(sext_i32(x), '032b'))
x = 0b0100_1111
print(format(sext_i32(x), '032b'))
x = 0b0100_1111_1111_0000
print(format(sext_i32(x,16), '032b'))
x = 0b1100_1111_1111_0000
print(format(sext_i32(x,16), '032b'))

def bitset0(x, offset):
    return x & (~(1 << offset))

def bitset1(x, offset):
    return x | (1 << offset)

print(bin(bitset0(0b1111,3)))
print(bin(bitset1(0b0000,3)))

def bitreplicate(x):
    tmp = x
    r = 0
    for i in range(0,32):
        if tmp & 1: 
            r = bitset1(r, i*2)
            r = bitset1(r, i*2 + 1)
        else:
            r = bitset0(r, i*2)
            r = bitset0(r, i*2 + 1)
        tmp >>= 1
    return r

x=0b0101_0101_0101_0101_0101_0101_0101_0101
print(format(bitreplicate(x), '064b'))

def bitcnt(x, bit=0, sz=32):
    tmp = 0
    for i in range(0, sz):
        if (x & 1 == bit):
            tmp += 1
        x >>= 1
    return tmp

# Get all the op code names.
def get_op_code_names(self):
    return self.instructions.keys()

print(bitcnt(x, bit=1))
print(bitcnt(0, bit=1))
print(bitcnt(0xFFFFFFFF, bit=1))
print(bitcnt(0xFFFFFFFFFFFFFFFF, bit=1, sz=64))
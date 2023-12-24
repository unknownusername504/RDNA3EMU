
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


print(cls(0, 32))
print(cls(0x0000cccc, 32))
print(cls(0xffff3333, 32))
print(cls(0x7fffffff, 32))
print(cls(0x80000000, 32))
print(cls(0xffffffff, 32))
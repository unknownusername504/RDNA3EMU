
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

# Example usage:
input_value_32 = 0b11011010101010101110100101010101  # Replace with your 32-bit integer
result_32 = rev_b32(input_value_32)
print(bin(result_32))

input_value_64 = 0b1101101010101010111010010101010110101010101010111101001010101010  # Replace with your 64-bit integer
result_64 = rev_b64(input_value_64)
print(bin(result_64))

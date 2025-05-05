# Write a Java/C/C++/Python program to implement DES algorithm.

# Initial permutation table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Final permutation (inverse of initial)
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

# Simple permutation function
def permute(bits, table):
    return [bits[i - 1] for i in table]

# Convert string to bit array
def string_to_bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:].zfill(8)
        result.extend([int(b) for b in bits])
    return result

# Convert bit array to string
def bits_to_string(b):
    chars = []
    for i in range(0, len(b), 8):
        byte = b[i:i+8]
        chars.append(chr(int(''.join(map(str, byte)), 2)))
    return ''.join(chars)

# Very simplified round (just swaps halves)
def simple_round(left, right, key):
    return right, [l ^ k for l, k in zip(left, key[:len(left)])]

# Simple DES encryption (1 round)
def simple_des_encrypt(plaintext, key):
    bits = string_to_bits(plaintext)
    bits = permute(bits, IP)
    left = bits[:32]
    right = bits[32:]
    key_bits = string_to_bits(key)

    left, right = simple_round(left, right, key_bits)

    combined = left + right
    final_bits = permute(combined, FP)
    return bits_to_string(final_bits)

# Simple DES decryption (1 round)
def simple_des_decrypt(ciphertext, key):
    bits = string_to_bits(ciphertext)
    bits = permute(bits, IP)
    left = bits[:32]
    right = bits[32:]
    key_bits = string_to_bits(key)

    right, left = simple_round(right, left, key_bits)

    combined = left + right
    final_bits = permute(combined, FP)
    return bits_to_string(final_bits)

# Example usage
plaintext = "SUJALG14"     # 8 characters = 64 bits
key = "ADGFHS56"           # 8 characters = 64 bits

cipher = simple_des_encrypt(plaintext, key)
print("Encrypted:", cipher)

original = simple_des_decrypt(cipher, key)
print("Decrypted:", original)


# Question: What is DES?
# Answer: DES (Data Encryption Standard) is a symmetric-key block 
# cipher that encrypts data in 64-bit blocks using a 56-bit key 
# over 16 rounds of processing.

# Question: What is implemented in this code?
# Answer: This code implements a very simplified version of DES, 
# using only 1 round of encryption and a simplified key mixing 
# and permutation logic.

# Question: Why is the initial permutation (IP) used?
# Answer: The IP rearranges the 64-bit plaintext to prepare 
# it for the DES rounds. It's part of the original DES structure 
# to improve diffusion.

# Question: What does the `permute()` function do?
# Answer: It rearranges bits according to a permutation table. 
# It's used for both initial and final permutations in DES.

# Question: What is the role of `string_to_bits()`?
# Answer: It converts each character of a string to its 8-bit 
# binary representation, forming a list of bits.

# Question: What does `bits_to_string()` do?
# Answer: It converts a list of bits back into a string by 
# grouping them into bytes and converting each to a character.

# Question: Why does DES use 64-bit blocks?
# Answer: DES was designed to process 64-bit blocks of data, 
# balancing security and performance for hardware in the 1970s.

# Question: What is simplified in this DES implementation?
# Answer: The full 16-round structure, expansion, S-boxes, 
# and full key schedule are removed. Only a simple XOR and 
# 1 round of left-right swapping are shown.

# Question: How is the `simple_round()` function working?
# Answer: It just swaps the halves and applies XOR between 
# the left half and part of the key bits.

# Question: What is the purpose of final permutation (FP)?
# Answer: FP is the inverse of IP. It brings the bits back 
# to the original order after rounds of encryption.

# Question: How are keys represented in this code?
# Answer: The key is an 8-character string converted to 
# a list of bits. This mimics the 64-bit DES key input.

# Question: Is this code secure like real DES?
# Answer: No. This is only a learning tool. Real DES uses 
# multiple rounds, substitution boxes, and key scheduling 
# for stronger encryption.

# Question: What is the significance of using XOR in the round?
# Answer: XOR is used to mix key bits with data bits. 
# It's reversible, which is crucial for decryption.

# Question: How does this code perform decryption?
# Answer: It reverses the encryption steps by swapping 
# halves back and reapplying the same XOR with the key.

# Question: What happens if the plaintext or key is not 8 characters?
# Answer: Since DES operates on 64-bit blocks, input must 
# be exactly 8 characters (8 bytes = 64 bits), or else 
# the code may fail or behave unpredictably.

# Question: What is the role of swapping halves?
# Answer: In real DES, swapping is part of the round 
# structure to enable mixing of the data across rounds.

# Question: How is this implementation helpful?
# Answer: It helps in understanding how DES works at 
# a high level — particularly permutations, bitwise 
# operations, and left-right processing.

# Question: What is the time complexity of this code?
# Answer: O(n), where n is the number of bits processed. 
# Since DES works on fixed-size blocks, it's constant 
# per block, i.e., O(1) per 64-bit block.

# Question: Can this be extended to full DES?
# Answer: Yes, but it would require implementing all 16 
# rounds, proper key schedule, expansion, S-boxes, and 
# Feistel function as defined in DES.

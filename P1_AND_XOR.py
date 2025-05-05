string = input("Enter String: ")
result_and = ""
result_xor = ""
for char in string:
    # Bitwise AND with 127 (removes 8th bit if present)
    and_val = ord(char) & 127
    result_and += chr(and_val)
    # Bitwise XOR with 127 (flips first 7 bits)
    xor_val = ord(char) ^ 127
    result_xor += chr(xor_val)
print("Original string: ", string)
print("AND result: ", result_and)
print("XOR result: ", result_xor)

# Question: What are bitwise operations in general?
# Answer: Bitwise operations are operations that directly manipulate 
# individual bits of binary numbers. These operations are typically used 
# for tasks that require low-level manipulation of data, such as encryption 
# and performance optimization.

# Question: What does the bitwise AND operation do?
# Answer: The bitwise AND operation compares each corresponding bit of two 
# numbers and returns 1 if both bits are 1, otherwise, it returns 0. In the 
# context of the code, ANDing with 127 effectively removes the 8th bit, 
# leaving only the lower 7 bits.

# Question: What is the bitwise XOR operation and how does it work?
# Answer: The bitwise XOR operation compares each corresponding bit of two 
# numbers and returns 1 if the bits are different, otherwise, it returns 0. 
# In the code, XORing with 127 flips the first 7 bits of the character's ASCII 
# value, creating a transformed result.

# Question: Why are bitwise operations commonly used in cryptography?
# Answer: Bitwise operations like AND and XOR are fast and efficient, making 
# them ideal for cryptographic algorithms. XOR, in particular, is useful in 
# creating simple ciphers because it can "flip" bits in a reversible way.

# Question: What is the significance of working with ASCII values in this code?
# Answer: ASCII values are numerical representations of characters. By performing 
# bitwise operations on these values, we can manipulate the underlying bits 
# of characters and create transformed or encrypted versions of the original text.

# Question: How does the code handle characters that are outside the ASCII range?
# Answer: The code assumes that characters are within the ASCII range (0-127). 
# If characters with values outside this range are entered, the bitwise operations 
# may lead to incorrect or unexpected results, as the operations are designed for 
# 7-bit ASCII characters.

# Question: Can bitwise operations be used for string encryption?
# Answer: Yes, bitwise operations like XOR are often used in simple encryption schemes, 
# such as the XOR cipher. However, such methods are not secure for modern cryptography 
# and are vulnerable to attacks.

# Question: What is the role of the number 127 in the code?
# Answer: 127 is used because it represents the binary value `01111111`, 
# which has the 8th bit (the most significant bit) set to 0. 
# ANDing with 127 removes the 8th bit, while XORing with 127 flips the first 7 bits.

# Question: Why is the XOR operation often used in encryption algorithms?
# Answer: XOR is widely used in encryption because it is reversible. If you 
# XOR the result with the same key again, you get back the original value. 
# This property is useful for simple encryption schemes, although it's not secure 
# for modern cryptography on its own.

# Question: What is the difference between AND and XOR operations in this context?
# Answer: In the context of the code, the AND operation with 127 removes the 
# 8th bit from the character's ASCII value, essentially converting it to a 7-bit 
# character. The XOR operation flips the first 7 bits of the character's ASCII 
# value, creating a completely different character.

# Question: Why is it important to know the bitwise operations when working with low-level data?
# Answer: Bitwise operations allow for direct manipulation of data at the 
# bit level, which is essential for tasks such as optimizing memory usage, 
# implementing cryptographic algorithms, and controlling hardware devices. 
# They are faster and more efficient compared to high-level operations.

# Question: What are the practical uses of bitwise AND and XOR in real-world applications?
# Answer: Bitwise AND and XOR are used in tasks such as data masking, 
# encryption (like the XOR cipher), error detection (parity checks), 
# and data compression. They are also used in network protocols and 
# device control where efficiency is critical.


# Function to encrypt the message using columnar transposition
def encrypt(message, key):
    encrypted = ""
    # Traverse column-wise
    for col in range(key):
        pointer = col
        while pointer < len(message):
            encrypted += message[pointer]
            pointer += key  # Move to the next row in the same column
    return encrypted

# Function to decrypt the cipher text using columnar transposition
def decrypt(ciphertext, key):
    num_rows = len(ciphertext) // key
    if len(ciphertext) % key != 0:
        num_rows += 1  # Add extra row if needed

    # Calculate how many empty boxes (shaded boxes) are in the last row
    num_shaded_boxes = (num_rows * key) - len(ciphertext)

    # Create a list to represent each row
    plaintext = [''] * num_rows
    col = 0
    row = 0

    for symbol in ciphertext:
        plaintext[row] += symbol
        row += 1

        # If we reach end of current column or we are at the last possible row for shorter column
        if (row == num_rows) or (row == num_rows - 1 and col >= key - num_shaded_boxes):
            row = 0
            col += 1

    return ''.join(plaintext)

# Main program starts here
message = input("Enter message: ").replace(" ", "")  # Remove spaces for simplicity
key = int(input("Enter key (number): "))

# Perform encryption
encrypted_msg = encrypt(message, key)
print("Encrypted:", encrypted_msg)

# Perform decryption
decrypted_msg = decrypt(encrypted_msg, key)
print("Decrypted:", decrypted_msg)


# Question: What is a transposition cipher?
# Answer: A transposition cipher is a type of encryption where 
# the positions of characters in the plaintext are shifted or 
# rearranged to create the ciphertext, without changing the characters themselves.

# Question: How does a transposition cipher differ from a substitution cipher?
# Answer: A substitution cipher changes the characters of the 
# plaintext to form ciphertext, while a transposition cipher 
# only rearranges the order of the characters, without altering them.

# Question: What are the different types of transposition ciphers?
# Answer: Some common types of transposition ciphers include 
# the columnar transposition, rail fence cipher, and route cipher.

# Question: Why are transposition ciphers considered less secure than modern ciphers?
# Answer: Transposition ciphers are considered less secure because 
# they do not change the characters themselves, so frequency analysis 
# and other cryptanalytic techniques can help break the cipher more easily.

# Question: What is the significance of the key in a transposition cipher?
# Answer: The key in a transposition cipher determines how the plaintext 
# is arranged into columns or rows. The key length and the method 
# used to rearrange the characters directly affect the cipher's strength.

# Question: What is a columnar transposition cipher?
# Answer: A columnar transposition cipher arranges the message into 
# a grid of columns based on the key. The ciphertext is created by 
# reading the characters column by column.

# Question: How can you decrypt a message encrypted with a transposition cipher?
# Answer: To decrypt a transposition cipher, you need to reverse the 
# transposition process by reconstructing the grid based on the key 
# and reading the characters in the correct order.

# Question: Why is the transposition cipher vulnerable to frequency analysis?
# Answer: Since the characters are not altered in a transposition cipher, 
# frequency analysis can be applied to the ciphertext to determine 
# patterns or clues that help in deciphering the message.

# Question: Can transposition ciphers be combined with substitution ciphers for better security?
# Answer: Yes, combining transposition ciphers with substitution ciphers 
# creates a more secure encryption system, as it makes it harder to apply 
# cryptanalytic techniques to break the cipher.

# Question: What are the main challenges in cracking a transposition cipher?
# Answer: The main challenge in breaking a transposition cipher is 
# determining the correct key and understanding how the plaintext 
# was rearranged. This can be tricky without enough ciphertext.

# Question: How does the columnar transposition cipher handle padding when the message length 
# is not divisible by the key?
# Answer: In columnar transposition, the message is padded with extra 
# characters (often 'X') to make the message length divisible by the key, 
# ensuring the grid is complete.

# Question: What is the time complexity of solving a transposition cipher?
# Answer: The time complexity for solving a transposition cipher depends 
# on the method used. A brute-force attack could require checking all 
# possible rearrangements, resulting in a time complexity of O(n!),
# where n is the length of the ciphertext.

# Question: What are some real-world applications of transposition ciphers?
# Answer: While transposition ciphers are largely obsolete for modern 
# encryption, they have historically been used for military communication 
# and are still studied for educational purposes in cryptography.

# ============================
# 1. XOR/AND String Encryption
# ============================

# Q1: What happens when you XOR a character with 127?
# A1: XOR with 127 inverts the most significant 7 bits of the character, producing an obfuscated form.

# Q2: What is the difference between AND and XOR operations on characters?
# A2: AND with 127 limits the character to 7 bits; XOR changes the bit pattern and is reversible.

# Q3: Why is XOR commonly used in encryption?
# A3: XOR is simple, reversible, and provides basic confidentiality when used with a key.

# Q4: Is XOR encryption secure?
# A4: Not by itself; it's vulnerable unless used with a one-time pad or strong key schedule.

# Q5: What is the result of applying XOR 127 twice?
# A5: The original value is restored (a ⊕ 127 ⊕ 127 = a).


# ============================
# 2. Transposition Cipher
# ============================

# Q6: What is a transposition cipher?
# A6: A cipher that rearranges the characters of the plaintext without changing the actual characters.

# Q7: Is the transposition technique symmetric or asymmetric?
# A7: It is symmetric; the same key can be used to encrypt and decrypt.

# Q8: How is a key used in transposition cipher?
# A8: The key determines the order of the columns or character rearrangement.

# Q9: How does decryption work in transposition cipher?
# A9: Reverse the columnar rearrangement using the same key.

# Q10: Can transposition be combined with substitution?
# A10: Yes, this makes the cipher more secure (e.g., product cipher).


# ============================
# 3. DES (Data Encryption Standard)
# ============================

# Q11: What is the key size in DES?
# A11: DES uses a 56-bit key (from a 64-bit input key with 8 bits for parity).

# Q12: How many rounds are there in DES?
# A12: DES performs 16 Feistel rounds.

# Q13: What is the block size of DES?
# A13: 64 bits.

# Q14: Is DES considered secure today?
# A14: No, it is vulnerable to brute-force attacks due to small key size.

# Q15: What does Feistel structure mean?
# A15: A symmetric structure where data is split into halves and processed in multiple rounds with swapping.


# ============================
# 4. AES (Advanced Encryption Standard)
# ============================

# Q16: What is the block size and key size in AES?
# A16: Block size is 128 bits; key sizes can be 128, 192, or 256 bits.

# Q17: How many rounds does AES use?
# A17: 10 for 128-bit keys, 12 for 192-bit, and 14 for 256-bit keys.

# Q18: Is AES symmetric or asymmetric?
# A18: Symmetric (same key for encryption and decryption).

# Q19: What are the major steps in AES?
# A19: SubBytes, ShiftRows, MixColumns, and AddRoundKey.

# Q20: Is AES secure?
# A20: Yes, widely trusted and used in modern encryption.


# ============================
# 5. RSA (Rivest–Shamir–Adleman)
# ============================

# Q21: What type of encryption is RSA?
# A21: Asymmetric; it uses a public and a private key.

# Q22: What is the basis of RSA security?
# A22: The difficulty of factoring large prime products.

# Q23: What are the key generation steps in RSA?
# A23: Choose two primes p, q → compute n=p*q → compute φ(n) → choose e → compute d such that e*d ≡ 1 mod φ(n).

# Q24: What is the formula for RSA encryption and decryption?
# A24: Encryption: c = m^e mod n; Decryption: m = c^d mod n.

# Q25: Is RSA used for both encryption and authentication?
# A25: Yes; encrypt with public key for secrecy, sign with private key for authentication.


# ============================
# 6. Diffie-Hellman Key Exchange (HTML + JS)
# ============================

# Q26: What is the purpose of Diffie-Hellman?
# A26: To securely exchange a shared secret key over an insecure channel.

# Q27: What is the mathematical principle behind Diffie-Hellman?
# A27: Discrete logarithm problem.

# Q28: Is Diffie-Hellman encryption?
# A28: No, it's a key exchange protocol, not an encryption algorithm.

# Q29: What values must be shared in Diffie-Hellman?
# A29: Prime number p and base g (both public).

# Q30: How does each party generate the shared key?
# A30: Each party chooses a private key, computes a public value, and derives the shared secret by raising the other’s public value to their private power mod p.

# Q31: How is JavaScript suitable for client-side Diffie-Hellman?
# A31: JS can dynamically compute values using BigInt and simulate real-time interaction with users.

# Q32: What is the main vulnerability of Diffie-Hellman?
# A32: Susceptibility to Man-in-the-Middle attacks if identity/authentication is not verified.

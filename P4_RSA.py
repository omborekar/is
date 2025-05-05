import math

# Function to check if a number is prime
def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return num > 1

# Generate RSA keys
def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Find e (public exponent)
    e = 3
    while math.gcd(e, phi) != 1:
        e += 2  # Try next odd number

    # Find d (private exponent)
    d = pow(e, -1, phi)

    return (e, n), (d, n)

# Encrypt text message
def encrypt(public_key, message):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

# Decrypt text message
def decrypt(private_key, encrypted_message):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in encrypted_message])

# Main program
print("Simple RSA Encryption/Decryption")
p = int(input("Enter a prime number p: "))
q = int(input("Enter another prime number q: "))

# Generate keys
public_key, private_key = generate_keys(p, q)

print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

message = input("Enter a message to encrypt: ")

# Encrypt and Decrypt
encrypted_message = encrypt(public_key, message)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(private_key, encrypted_message)
print("Decrypted Message:", decrypted_message)


# I/P : 17, 11, hi/hello

# Question: What is RSA?
# Answer: RSA is an asymmetric cryptographic algorithm 
# that uses two keys — a public key for encryption 
# and a private key for decryption.

# Question: What does the `is_prime()` function do?
# Answer: It checks if a number is prime by testing 
# divisibility up to the square root of the number.

# Question: Why must p and q be prime?
# Answer: In RSA, p and q must be prime to ensure 
# security and correct calculation of φ(n), which 
# is used in key generation.

# Question: What is φ(n) (Euler's totient function)?
# Answer: For RSA, φ(n) = (p−1)(q−1). It represents 
# the count of integers less than n that are coprime to n.

# Question: Why is e chosen such that gcd(e, φ(n)) = 1?
# Answer: So that e and φ(n) are coprime, allowing 
# a modular inverse `d` to exist for decryption.

# Question: What does the `generate_keys()` function return?
# Answer: It returns a public key (e, n) and a private 
# key (d, n), used for encryption and decryption.

# Question: What does the `encrypt()` function do?
# Answer: It converts each character of the message 
# to its ASCII value, raises it to the power `e`, 
# and takes mod `n`.

# Question: What does the `decrypt()` function do?
# Answer: It reverses encryption using the private key 
# by computing (cipher^d) mod n and converting the 
# result back to characters.

# Question: Why is modular exponentiation used?
# Answer: It prevents overflow and keeps computations 
# within a practical range, essential for secure encryption.

# Question: What is the role of `pow(base, exp, mod)` in Python?
# Answer: It efficiently computes (base^exp) % mod using 
# modular exponentiation, which is optimized internally.

# Question: How is the private exponent `d` calculated?
# Answer: It is the modular inverse of `e` modulo φ(n), 
# meaning (d * e) % φ(n) = 1.

# Question: What is `n` used for in RSA?
# Answer: `n` is the modulus for both keys and is the 
# product of two large primes. It defines the numeric 
# space of the encryption.

# Question: What happens if `e` and φ(n) are not coprime?
# Answer: The modular inverse `d` won't exist, and RSA 
# decryption will fail.

# Question: Is this code secure for real-world use?
# Answer: No. It's a simplified example. Real RSA uses 
# large primes (hundreds of digits) and includes 
# padding (like OAEP) for security.

# Question: Can we use the same key pair for multiple messages?
# Answer: Yes, the same key pair can encrypt and decrypt 
# multiple messages unless new keys are regenerated.

# Question: What type of cryptography does RSA use?
# Answer: RSA is public-key (asymmetric) cryptography, 
# where encryption and decryption use different keys.

# Question: Why are two keys needed in RSA?
# Answer: One key (public) is used to encrypt, while 
# the other (private) is used to decrypt, enhancing 
# both confidentiality and secure communication.

# Question: What is the time complexity of RSA operations?
# Answer: Encryption and decryption are based on modular 
# exponentiation, which is efficient using fast exponentiation. 
# However, key generation can be costly with large primes.

# Question: What kind of attacks can break RSA?
# Answer: RSA can be broken by factoring n, which is hard 
# for large n. Weak keys, small e, and lack of padding 
# make it vulnerable to attacks like chosen ciphertext attacks.


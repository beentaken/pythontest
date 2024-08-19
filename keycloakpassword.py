
import hashlib
import binascii

# Update the below accordingly
password = "P@ssw0rd"
provided_salt = "vQxVDx9PBVmqDfvae3z/zg=="

# Convert the salt from base64 to bytes
salt = binascii.a2b_base64(provided_salt)

# Number of iterations for PBKDF2
hash_iterations = 27500

# Hash the password using PBKDF2-SHA256
hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, hash_iterations,64)

# Convert the hash to a base64-encoded string
hashed_password_base64 = binascii.b2a_base64(hashed_password).decode('utf-8').rstrip('\n')

print("Hashed password_base64:", hashed_password_base64)

# Update the below accordingly
password = "P@ssw0rd"
provided_salt = "xpph7zA/tHG5AbfnRyMn9g=="

# Convert the salt from base64 to bytes
salt = binascii.a2b_base64(provided_salt)

# Number of iterations for PBKDF2
hash_iterations = 27500

# Hash the password using PBKDF2-SHA256
hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, hash_iterations,64)

# Convert the hash to a base64-encoded string
hashed_password_base64 = binascii.b2a_base64(hashed_password).decode('utf-8').rstrip('\n')

print("Hashed password_base64:", hashed_password_base64)

# Update the below accordingly
password = "P@ssw0rd123"
provided_salt = "rTNpYoyEdmsvQxlugslSDg=="

# Convert the salt from base64 to bytes
salt = binascii.a2b_base64(provided_salt)

# Number of iterations for PBKDF2
hash_iterations = 27500

# Hash the password using PBKDF2-SHA256
hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, hash_iterations,64)

# Convert the hash to a base64-encoded string
hashed_password_base64 = binascii.b2a_base64(hashed_password).decode('utf-8').rstrip('\n')

print("Hashed password_base64:", hashed_password_base64)


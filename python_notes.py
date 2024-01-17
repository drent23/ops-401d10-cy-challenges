# From Roger's class 6 lecture

# Declare functions
def encrypt(number, key):
    encrypted_text = ""

    for num in number:
        numb = int(num, 16)
        shifted_num = (numb + key) % 10
        encrypted_text += str(shifted_num)
    return encrypted_text

def decrypt(encoded, key):
    return encrypt(encoded, -key)

if __name__ == "__main__":
    encrypted = encrypt('123456', 3)
    print(encrypted)
    decrypted = decrypt(encrypted, 3)
    print(decrypted)

# must pip install cryptography package library then import Fernet module from it
from cryptography.fernet import Fernet

# generate key
key = Fernet.generate_key()

# assign key value to var
f = Fernet(key)

# convert PT to CT, 
token = f.encrypt(b"encryption is fun")

# 'b' = byte format, in this case binary...this can be removed using decode() method while printing original message (in libary's internal method)

#  display CT
print(token)

# decrypt CT
d = f.decrypt(token)

# display PT
print(d)

# generate key and save to file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

# loads key from current directory named 'key.key'
def load_key():
    return open("key.key", "rb").read()

# generate and write a new key
write_key()

# load previously generated key
key = load_key()
print("Key is " + str(key.decode('utf-8')))

message = "hello friend".encode()
print("PT is " + str(message.decode('utf-8')))

# initialize Fernet class
f = Fernet(key)

# encrypt the message
encrypted = f.encrypt(message)

# print how it looks
print("CT is " + encrypted.decode('utf-8'))

# Roger's class 7 warmup & lecture

import os

# '.' tells python to run walk specifically from current directory
import os
for root, dirs, files in os.walk("."):
    print(root)
    print(dirs)
    print(files)
    # 
    print('-' * 88)
for root, dirs, files in os.walk("/home/david"):
    print(root)
    print(dirs)
    print(files)
    print('-' * 88)
for root, dirs, files in os.walk("/home/david"):
    print(root)
    print(dirs)
    print(files)
    for file in files:
        with open(file) as f:
            print(f.read())
    print('-' * 88)
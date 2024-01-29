#!/usr/bin/env python3

# Script Name: Encrypt/Decrypt File/Message
# Author: David Renteria
# Purpose: Get user to input target file or string to encrypt/decrypt

# import Fernet & os modules
from cryptography.fernet import Fernet
import os

# declare functions

# load or generate key and save to file
def gen_key():
    try:
        with open("key.key", "rb") as key_file:
            secret_key = key_file.read()
    except FileNotFoundError: 
        secret_key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(secret_key)
    return secret_key
    

# encrypt file, delete existing version, and replace w/ encrypted version
def encrypt_file(target_file, secret_key):
    f = Fernet(secret_key)
    with open(target_file, "rb") as key_file:
        dec_data = key_file.read()
    enc_data = f.encrypt(dec_data)
    os.remove(target_file)
    with open(target_file, "wb") as key_file:
        key_file.write(enc_data)

# decrypt file, delete encrypted version, and replace w/ decrypted version
def decrypt_file(target_file, secret_key):
    f = Fernet(secret_key)
    with open(target_file, "rb") as key_file:
        enc_data = key_file.read()
    dec_data = f.decrypt(enc_data)
    os.remove(target_file)
    with open(target_file, "wb") as key_file:
        key_file.write(dec_data)

# mode 3, prompt user for PT string, encrypt, print/display CT string
def encrypt_msg(dec_msg, secret_key):
    f = Fernet(secret_key)
    enc_msg = f.encrypt(dec_msg.encode())
    return enc_msg

# mode 4, prompt user for CT string, decrypt, print/display PT string
def decrypt_msg(enc_msg, secret_key):
    f = Fernet(secret_key)
    dec_msg = f.decrypt(enc_msg)
    return dec_msg.decode()

# compress files
def compress_file(target_file):
    file_name = f"{target_file}.tar.gz"
    os.system(f"tar -czf {file_name} {target_file}")
    return file_name

# main function
def main():
    secret_key = gen_key()
    user_mode = input("Please select whether you'd like to encrypt/decrypt a file or message: \n1 - Encrypt a file\n2 - Decrypt a file\n3 - Encrypt a message\n4 - Decrypt a message\n")
    # conditionals based on user input
    if user_mode == '1':
        target_file = input("Please enter the path of your target file you want to encrypt: ")
        encrypt_file(target_file, secret_key)
        if input("Would you like to compress the file as well? (Enter 'y' for yes or 'n' for no): ") == 'y':
            file_compress = compress_file(target_file)
            print(f"The file has been compressed and is now named {file_compress}")
    elif user_mode == '2':
        target_file = input("Please enter the path of your target file you want to decrypt: ")
        decrypt_file(target_file, secret_key)
        if input("Would you like to compress the file as well? (Enter 'y' for yes or 'n' for no): ") == 'y':
            file_compress = compress_file(target_file)
            print(f"The file has been compressed and is now named {file_compress}")
    elif user_mode == '3':
        msg = input("Please enter a simple string you'd like to encrypt: ")
        encrypted_msg = encrypt_msg(msg, secret_key)
        print(f"The encrypted string is as follows: {encrypted_msg}")
    elif user_mode == '4':
        encrypted_msg = input("Please enter the encrypted string you'd like to decrypt: ").encode()
        decrypted_msg = decrypt_msg(encrypted_msg, secret_key)
        print(f"The decrypted string is as follows: {decrypted_msg}")
    else:
        print("Please only enter a number between 1 - 4.")

if __name__ == "__main__":
    main()
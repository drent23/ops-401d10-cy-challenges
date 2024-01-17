#!/usr/bin/env python3

# Script Name: Encrypt/Decrypt File/Message/Folder(s) Recursively
# Author: David Renteria
# Purpose: Get user to input target file, string, or folder to encrypt/decrypt

# import Fernet & os modules
from cryptography.fernet import Fernet
import os

# declare functions

# generate key and save to file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

# loads key from current directory named 'key.key'
def load_key():
    return open("key.key", "rb").read()

# mode 1, prompt user for target file path, encrypt file, delete existing version, and replace w/ encrypted version
def enc_file(target_file):
    key = load_key()
    f = Fernet(key)

    with open(target_file, "rb") as file:
        dec_data = file.read()
    enc_data = f.encrypt(dec_data)
    os.remove(target_file)
    with open(target_file, "wb") as file:
        file.write(enc_data)

# mode 2, prompt user for target file path, decrypt file, delete encrypted version, and replace w/ decrypted version
def dec_file(target_file):
    key = load_key()
    f = Fernet(key)

    with open(target_file, "rb") as file:
        enc_data = file.read()
    dec_data = f.decrypt(enc_data)
    os.remove(target_file)
    with open(target_file, "wb") as file:
        file.write(dec_data)

# mode 3, prompt user for PT string, encrypt, print/display CT string
def enc_msg(msg):
    key = load_key()
    f = Fernet(key)
    encrypted_msg = f.encrypt(msg.encode())
    return encrypted_msg

# mode 4, prompt user for CT string, decrypt, print/display PT string
def dec_msg(msg):
    key = load_key()
    f = Fernet(key)
    decrypted_msg = f.decrypt(msg)
    return decrypted_msg.decode()

# mode 5, prompt user for target folder and encrypt it and all its contents (recursive)
def enc_folder(target_folder, key):
    key = load_key()
    # loop through root, dirs, & files then walk 
    for root, dirs, files, in os.walk(target_folder):
        for file in files:
            target_file = os.path.join(root, dirs, file)
            enc_file(target_file, key)    

# mode 6, prompt user for target folder and decrypt it recursively 
def dec_folder(target_folder, key):
    key = load_key()
    # loop through root, dirs, & files then walk 
    for root, dirs, files, in os.walk(target_folder):
        for file in files:
            target_file = os.path.join(root, dirs, file)
            dec_file(target_file, key)

# compress files
def compress_file(target_file):
    file_name = f"{target_file}.tar.gz"
    os.system(f"tar -czf {file_name} {target_file}")
    return file_name

# main function
def main():
    key = load_key()
    user_mode = input("Please select whether you'd like to encrypt/decrypt a file or message: \n1 - Encrypt a file\n2 - Decrypt a file\n3 - Encrypt a message\n4 - Decrypt a message\n5 - Encrypt a folder\n6 - Decrypt a folder\n")
    # conditionals based on user input
    if user_mode == '1':
        target_file = input("Please enter the path of your target file you want to encrypt: ")
        enc_file(target_file)
        if input("Would you like to compress the file as well? (Enter 'y' for yes or 'n' for no): ") == 'y':
            file_compress = compress_file(target_file)
            print(f"The file has been compressed and is now named {file_compress}")
    elif user_mode == '2':
        target_file = input("Please enter the path of your target file you want to decrypt: ")
        dec_file(target_file)
        if input("Would you like to compress the file as well? (Enter 'y' for yes or 'n' for no): ") == 'y':
            file_compress = compress_file(target_file)
            print(f"The file has been compressed and is now named {file_compress}")
    elif user_mode == '3':
        msg = input("Please enter a simple string you'd like to encrypt: ")
        encrypted_msg = enc_msg(msg)
        print("The encrypted string is as follows: ", encrypted_msg.decode())
    elif user_mode == '4':
        msg = input("Please enter the encrypted string you'd like to decrypt: ")
        decrypted_msg = dec_msg(msg)
        print("The decrypted string is as follows: ", decrypted_msg)
    elif user_mode == '5':
        target_folder = input("Please inter the path to the target folder you want to encrypt: ")
        enc_folder(target_folder, key)
        print(f"Your target folder {target_folder} and its contents have been encrypted!")
    elif user_mode == '6':
        target_folder = input("Please enter the path of your target folder you want to decrypt: ")
        dec_folder(target_folder, key)
        print(f"Your target folder {target_folder} and its contents have been decrypted!")
    else:
        print("Please only enter a number between 1 - 4.")

if __name__ == "__main__":
    main()
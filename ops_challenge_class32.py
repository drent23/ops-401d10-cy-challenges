#!/usr/bin/env python3

# Script Name: Sig-based Malware detection pt 2
# Author: David Renteria
# Purpose: Basic Python AV tool w/ hash validation

# import modules
from sys import platform
import os, datetime, logging, hashlib

# configure logs
logging.basicConfig(filename='malware_threat.log',level=logging.INFO, filemode='w', format='%(asctime)s - %(levelname)s -%(message)s')


# declare function

# function to take file name & produce a hash for its contents
def hash_file(target_file):
    # create hash object
    hash = hashlib.sha512()

    # implement error handling
    try:
    # open file for reading in binary mode
        with open(target_file, 'rb') as file:
            # loop through end of file
            chunk = 0
            while chunk != b'':
                # read 1024 bytes at a time
                chunk = file.read(2048)
                print(chunk)
                hash.update(chunk)
        # return hex represenation of hash
        return hash.hexdigest()
    except Exception as e:
        logging.error(f"There was an error creating the hash: {e}")
        return None
    
# Function that handles search for both Linux & Windows using os.walk & os.path feature
def file_search(target_file, directory):
    searched_files = 0
    hits_found = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            searched_files += 1
            if file == target_file:
                hits_found += 1
                path = os.path.join(root, file)
                hash = hash_file(path)
                size = os.path.getsize(path)
                time = datetime.now()

                print(f"Time: {time}\nFile name: {file}\nFile path: {path}\nSize: {size}\nSHA512 hash: {hash}")
                logging.info((f"File path: {path}\nSHA512 hash: {hash}"))
    print(f"The number of files that were searched is: {searched_files}")
    print(f"The number of hits found is: {hits_found}")
    logging.info(f"# of searched files: {searched_files}; Hits found: {hits_found}; Target file path: {path}")

# prompt user for target file & directory and search system directory
target_file = input("Please enter the filename are you searching for: ")
directory = input("Please enter the directory you want to search in: ")

# OS system check & call function
if platform == "linux" or platform == "linux2":
    print("This is a Linux machine")
    file_search(target_file, directory)
elif platform == "win32":
    print("This is a Windows machine")
    file_search(target_file, directory)

# substitute file name for the function (another way)
# msg = hash_file("file.log")
# print(msg)
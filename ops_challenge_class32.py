#!/usr/bin/env python3

# Script Name: Sig-based Malware detection pt 2
# Author: David Renteria
# Purpose: Basic Python AV tool w/ hash validation

# import modules
from sys import platform
import os, time, logging, hashlib

# declare function

# function to take file name & produce a hash for its contents
def hash_file(target_file):
    # create hash object
    hash = hashlib.sha256()

    # open file for reading in binary mode
    with open(target_file, 'rb') as file:
        # loop through end of file
        chunk = 0
        while chunk != b'':
            # read 1024 bytes at a time
            chunk = file.read(1024)
            print(chunk)
            hash.update(chunk)
    # return hex represenation of hash
    return hash.hexdigest()

# substitute file name for the function
msg = hash_file("file.log")
print(msg)
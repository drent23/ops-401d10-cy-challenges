#!/usr/bin/env python3

# Script Name: Port Scanner with Rotating Log based on Size & Time and both File & Stream Handlers
# Author: David Renteria
# Purpose: Tool that uses scapy to scan ports then rotates logs based on time and size and outputs File Handlers to log files and Stream Handlers to display to screen

# import modules
from sys import platform
import os, time

# declare functions

# Function that handles Linux search
# def linux_search():
#     whichFile = input("What file are you searching for?")
#     directory = input("Which directory do you want to search in?")
#     os.system("Find " + str(directory) + " | echo 'Searched $(wc -l) files.\'")
#       call hash_function in here
# Function that handles Windows search
# def win_search():
#       call hash_function in here
# def hash_function 
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

# OS system check
if platform == "linux" or platform == "linux2":
    print("This is a Linux machine")
    # linux_search()
elif platform == "win32":
    print("This is a Windows machine")
    # win_search()


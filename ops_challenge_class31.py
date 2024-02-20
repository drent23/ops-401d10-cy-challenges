#!/usr/bin/env python3

# Script Name: Sig-based Malware detection pt 1
# Author: David Renteria
# Purpose: Basic Python AV tool

# import modules
from sys import platform
import os, time, logging

# configure logs
logging.basicConfig(filename='malware_threat.log',level=logging.INFO, filemode='w', format='%(asctime)s - %(levelname)s -%(message)s')

# declare functions

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
                print(f"The path to the file you requested is as follows: {path}")
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
#!/usr/bin/env python3

# Script Name: Brute Force Wordlist Attack Tool Pt 2
# Author: David Renteria
# Purpose: Tool that uses both offensive & defensive dictionary attack tactics by authenticating to an SSH server by its IP address

# Roger's lecture notes
from zipfile import ZipFile
def unzip_file(zipped_file):
    password = "password1234"
    with ZipFile(zipped_file) as f:
        f.extractall(pwd=bytes(password, 'utf-8'))
        print(f'The file {zipped_file} has been unzipped.')

if __name__ == '__main__ ':
    zip -er "filename.zip" "filename.txt"
    unzip_file("filename.zip")
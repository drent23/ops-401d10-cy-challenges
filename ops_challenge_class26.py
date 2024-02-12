#!/usr/bin/env python3

# Script Name: Brute Force Wordlist Attack Tool Pt 3
# Author: David Renteria
# Purpose: Tool that uses both offensive & defensive dictionary attack tactics by authenticating to an SSH server by its IP address and then zipping/unzipping that file

# import modules
import logging

# Create log object
log = logging.getLogger("data_logger")

# Config logging object
logging.basicConfig(filename='bruteforce.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')


log.info("Hello, world")
log.warning("This is a warning")
log.critical("This is critical")

# Define a function
def log_job():
    log.debug("Logging something")

# Call function
log_job()   
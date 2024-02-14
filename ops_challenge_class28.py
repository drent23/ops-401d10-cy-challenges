#!/usr/bin/env python3

# Script Name: Port Scanner with Rotating Log based on Size & Time and both File & Stream Handlers
# Author: David Renteria
# Purpose: Tool that uses scapy to scan ports then rotates logs based on time and size and outputs File Handlers to log files and Stream Handlers to display to screen

# import modules
import logging, time, os
from scapy.all import IP, sr1,TCP, send
import random
from logging.handlers import RotatingFileHandler
# from logging.handlers import TimedRotatingFileHandler for time based

# Assign target IP and port range to vars
host = 'scanme.nmap.org'
port_range = [20, 21, 22, 23, 53, 69, 80, 123, 179, 264, 443, 520]

# Config logging object based on size
logging.basicConfig(filename='bruteforce_size.log',level=logging.DEBUG, filemode='w', format='%(asctime)s - %(levelname)s -%(message)s')

# Config logging object based om time
# logging.basicConfig(filename='bruteforce_time.log',level=logging.DEBUG, filemode='w', format='%(asctime)s - %(levelname)s -%(message)s')

# Create log object named 'data_logger'
log = logging.getLogger('data_logger')

# Create handlers
# file handler and set level of msg to capture
file_handler = logging.FileHandler('bruteforce.log')
file_handler.setLevel(logging.WARNING)

# stream handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)

# Create formatters for handlers
file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# config formatters to apply to specific handler
file_handler.setFormatter(file_format)
stream_handler.setFormatter(stream_format)

# connect logger to handlers
log.addHandler(file_handler)
log.addHandler(stream_handler)

# Define a port scanning function
def scan_ports(dst_port):
    src_port = random.randint(1024, 65535)
    response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='S'), timeout=1, verbose=0)
    # conditionals to perform task based on port status
    if response is None:
        result = f"Port {dst_port} is filtered and silently dropped"
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:
            send(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='R'), verbose=0)
            result = f"Port {dst_port} is open"
        elif response.getlayer(TCP).flags == 0x14:
            result = f"Port {dst_port} is closed"
    log.debug(result)

# Define a logging function
def log_job(host, port_range):
    # create for loop to scan each port within the port range
    for port in port_range:
        try:
            result = scan_ports(host, port)
            log.info(result)
        except Exception as e:
            log.error(f"We ran into the following error at port {port}: {e}")

# Call function
log_job(host, port_range)
#!/usr/bin/env python3

# Script Name: Port Scanner with Logging
# Author: David Renteria
# Purpose: Tool that uses scapy to scan ports then logs them to a file

# import modules
import logging
from scapy.all import IP, sr1,TCP, send
import random

# Assign target IP and port range to vars
host = 'scanme.nmap.org'
port_range = [20, 21, 22, 23, 53, 69, 80, 123, 179, 264, 443, 520]

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
    return result

# Create log object
log = logging.getLogger("data_logger")

# Config logging object
logging.basicConfig(filename='bruteforce.log',level=logging.DEBUG, filemode='w', format='%(asctime)s - %(levelname)s -%(message)s')

# Define a logging function
def log_job(host, port_range):
    # create for loop to scan each port within the port range
    for port in port_range:
        try:
            result = scan_ports(host, port_range)
            log.info(result)
            log.debug(result)
            log.warning(result)
            log.critical(result)
        except Exception as e:
            log.error(f"We ran into the following error at port {port}: {e}")

# Call function
log_job(host, port_range)
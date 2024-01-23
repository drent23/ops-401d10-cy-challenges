#!/usr/bin/env python3

# Script Name: Create Nmap using Scapy
# Author: David Renteria
# Purpose: Scan network using Scapy

# import necessary modules
import sys
from scapy.all import IP, sr1, TCP, send
import random

# assign target IP and port range to vars
host = 'scanme.nmap.org'
port_range = [20, 21, 22, 23, 53, 69, 80, 123, 179, 264, 443, 520]

# define function to scan ports
def scan_ports(dst_port):
    src_port = random.randint(1024, 65535)
    response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='S'), timeout=1, verbose=0)
    # conditionals to perform task based on port status
    if response is None:
        print(f"Port {dst_port} is filtered and silently dropped")
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:
            send(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='R'), verbose=0)
            print(f"Port {dst_port} is open")
        elif response.getlayer(TCP).flags == 0x14:
            print(f"Port {dst_port} is closed")

# create for loop to scan each port within the port range
for port in port_range:
    scan_ports(port)
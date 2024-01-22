#!/usr/bin/env python3

# Script Name: Create Nmap using Scapy
# Author: David Renteria
# Purpose: Scan network using Scapy

# import necessary modules
import sys
from scapy.all import Ether, IP, sniff, ARP, sr1, ICMP, TCP
import random

# assign target IP and port range to vars
host = 'scanme.nmap.org'
port_range = [20-23, 80, 443]

# define function to scan ports
def scan_ports(dst_port):
    src_port = random.randint(1024, 65535)
    response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='5'), timeout=1, verbose=0)
    # conditionals to perform task based on port status
    if response is None:
        print(f"Port {dst_port} is filtered and silently dropped")
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:
            rst_packet = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='5'), timeout=1, verbose=0)
            send(rst_packet, verbose=0)
            print(f"Port {dst_port} is open")
        elif response.getlayer(TCP).flags == 0x14:
            print(f"Port {dst_port} is closed")

# create for loop to scan each port within the port range
for port in port_range:
    scan_ports(port)
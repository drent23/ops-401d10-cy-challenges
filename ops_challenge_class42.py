#!/usr/bin/env python3

# Script Name: Nmap Scanner Python Tool
# Author: David Renteria
# Purpose: Nmap scanner tool as part of pentester toolkit

# import modules
import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) TCP Scan             \n""") ### TODO: Select what your third scan type will be
print("You have selected option: ", resp)

range = '1-50'

### TODO: Prompt the user to type in a port range for this tool to scan
user_range = input("Please enter a range of port numbers to scan: ")
if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    ### TODO: Add missing code block here
    print("Please enter a valid option") ### TODO: Remove this
elif resp == '3':
    ### TODO: Add missing code block here
    print("Please enter a valid option") ### TODO: Remove this
elif resp >= '4':
    print("Please enter a valid option")
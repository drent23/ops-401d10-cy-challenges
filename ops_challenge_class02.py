#!/usr/bin/env python3

# Script: Uptime Sensor Configuration
# Purpose: Create a sensor tool that checks systems are responding appropriately
# Why: Critical aspect of security operations and network/security monitoring

# Import necessary libraries & modules
from ping3 import ping
import datetime
import time

# accept user input for target IP then transmit single ICMP (ping) packet to target IP every 2 seconds, evaluate response as success or failure, assign success or failure to status var, print status var along w/ timestamp & dest IP tested
def user_ip():
    target_ip = input("Please enter the IP address you want to test: ") or "8.8.8.8"
    return target_ip

def main():
    target_ip = user_ip()
    while True:
        try:
            response = ping(target_ip, timeout=1)
            status = "Success" if response is not None else "Failure"
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            print(f"{timestamp} {status} to {target_ip}")

        except Exception as e:
            print(f"Network error: {e}")
        time.sleep(2)

if __name__ == "__main__":
    main()
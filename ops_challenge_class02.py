#!/usr/bin/env python3

# Script: Uptime Sensor Configuration
# Purpose: Create a sensor tool that checks systems are responding appropriately
# Why: Critical aspect of security operations and network/security monitoring

# Import necessary libraries & modules
from pythonping import ping
import datetime
import time

# accept user input for target IP then transmit single ICMP (ping) packet to target IP every 2 seconds, evaluate response as success or failure, assign success or failure to status var, print status var along w/ timestamp & dest IP tested

import time
from ping3 import ping

# Function to get the target IP from user input or default to "8.8.8.8"
def user_ip():
    target_ip = input("Please enter the IP address you want to test: ") or "8.8.8.8"
    return target_ip

# Function to monitor network uptime for a given target IP
def main():
    target_ip = user_ip()
    while True:
        try:
            # Ping the target IP with a timeout of 1 second
            response = ping(target_ip, timeout=1)

            # Determine the network status based on the response
            status = "Success" if response is not None else "Failure"

            # Get the current timestamp
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

            # Save the timestamp, network status, and target IP to a file
            print(f"{timestamp} {status} to {target_ip}")

        except Exception as e:
            # Print an error message if an exception occurs
            print(f"Network error: {e}")
        time.sleep(2)

if __name__ == "__main__":
    main()
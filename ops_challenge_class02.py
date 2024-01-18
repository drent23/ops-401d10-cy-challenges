#!/usr/bin/env python3

# Script: Uptime Sensor Configuration
# Purpose: Create a sensor tool that checks systems are responding appropriately
# Why: Critical aspect of security operations and network/security monitoring

# Import necessary libraries & modules
from pythonping import ping
import datetime
import time

# accept user input for target IP then transmit single ICMP (ping) packet to target IP every 2 seconds, evaluate response as success or failure, assign success or failure to status var, print status var along w/ timestamp & dest IP tested

def eval_response(target_ip):
    try:
        response = ping(target_ip, count=1, timeout=2)
        if response == response.success():
            return "Success"
        else:
            return "Failure"
    except Exception as e:
        return f"Network error: {e}" 
    
def main():
    target_ip = input("Please enter the IP address of the host you want to ping: ") or "8.8.8.8"
    log_file = "ping_test.txt"

    with open(log_file, "a") as file:
        while True:
            status = eval_response(target_ip)
            timestamp = datetime.datetime.now()
            log_data = f"{timestamp} {status} to {target_ip}\n"
            print(log_data, end="")
            file.write(log_data)
            time.sleep(2)

if __name__ == "__main__":
    main()
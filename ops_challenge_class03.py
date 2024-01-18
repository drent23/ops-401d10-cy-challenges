#!/usr/bin/env python3

# Script: Uptime sensor pt 2
# Purpose: Implement email notifications for status changes
# Why: Keep administrators/users aware of network status changes as part of monitoring process
from ping3 import ping
import datetime
import time
import smtplib
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
#!/usr/bin/env python3

# Script: Uptime sensor pt 2
# Author: David Renteria
# Purpose: Implement email notifications for status changes
# Why: Keep administrators/users aware of network status changes as part of monitoring process

# import necessary libs/modules
import time  
from datetime import datetime  
import os  
from ping3 import ping  
import smtplib
from email.mime.text import MIMEText

# create var for user email
user_email = 'bob@gmail.com'

# ping target IP
def get_status(target_ip):
    response = ping(target_ip, timeout=1)
    return response is not None

# log ping/network status
def log_status(target_ip, timestamp, status):
    # data displayed in log file
    log_data = f"{timestamp} - IP {target_ip} is {'up' if status else 'down'})"

    # create log file and save to desktop
    log_file = os.path.join(os.path.expanduser("~"), "Desktop", "event_log.txt")
    with open(log_file, 'a') as file:
        file.write(log_data + '\n')

# send email using SMTP
def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'bob@gmail.com'
    msg['To'] = user_email

    # use email pw to authenticate
    email_password = ''
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('bob@gmail.com', email_password)
        server.sendmail('bob@gmail.com', [user_email], msg.as_string())

def main():
    # get target IP from user & ping every 2 seconds
    target_ip = input("Please enter the target IP address you'd like to check: ")
    while True:
        # Check the status of the host, use conditional to check previous status (used chatgpt for this part), log status, and create/send email
        status = get_status(target_ip)
        if hasattr(main, "previous_status") and main.previous_status != status:
            # use current DTG
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # log status of IP address
            log_status(target_ip, timestamp, status)

            # input subject & body then send email
            subject = f"Host Status Changed: {target_ip}"
            body = f"Host status changed at {timestamp}\n\nPrevious Status: {'Up' if main.previous_status else 'Down'}\nCurrent Status: {'Up' if status else 'Down'}"
            send_email(subject, body)
        
        # set the current status as the previous status for the next iteration (used chatgpt for this part too)
        main.previous_status = status
        
        # wait 2 seconds before next iteration
        time.sleep(2)

if __name__ == "__main__":
    main()
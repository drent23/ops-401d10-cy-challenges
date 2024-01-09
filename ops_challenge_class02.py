#!/usr/bin/env python3

# Script: Uptime Sensor Configuration
# Purpose: Create a sensor tool that checks systems are responding appropriately
# Why: Critical aspect of security operations and network/security monitoring

# Import necessary libraries & modules
import time
import datetime
import os
import subprocess
from pythonping import ping
import numpy

# accept user input for target IP then transmit single ICMP (ping) packet to target IP every 2 seconds

def ping_target():
    target_ip = input("Please enter the IP address of the host you want to ping: ")
    ping_logs = "ping logs.txt"
    with open(ping_logs, "a") as b:
        while True:
            current_time = datetime.datetime.now()
            # evaluate response as either success or failure
            try: 
                result = ping(target_ip, count=1, timeout=2)
                if result.rtt_avg_ms is not None:
                    # assign success or failure to 'status' variable
                    status = "Success"
                else: 
                    status = "Failure"
            except Exception as e:
                status = "Network is Inactive"
            
            # For every ICMP (ping) attempt, print status w/ timestamp & target IP
            log_data = f"{current_time} {status} to {target_ip}\n"
            print(log_data, end="")
            # save (write) 'log_data' to 'ping_logs' txt file
            b.write(log_data)
            time.sleep(2)
if __name__ == "__main__":
    ping_target



# def my_function(my_list = [5, 4, 3, 2, 1]):
#    for number in my_list:
#        print(number)
    # pass

# import datetime
# now = datetime.datetime.now()
# print(now)

# new_date = datetime.date(1999, 12, 31)
# print(new_date)

# import time

# time_now = time.localtime() # tiime.time()
# print(time_now)

# time.sleep(5)
# print('Did I sleep for 5 seconds')

# import os
# result = os.system('ping localhost -c 4')


# if __name__ == "__main__":
#    my_variable = [1, 2, 3, 4, 5]
#    my_function(my_variable)
#    my_function()
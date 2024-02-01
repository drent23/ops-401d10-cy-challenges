#!/bin/bash

# Marcus' version (log file already in directory)
grep "WARNING" $1 > "warning_logs.txt"
grep "THREAT" $1 > "threat_logs.txt"
grep "ERROR" $1 > "error_logs.txt"

# Cody's version (cat log file first)
cat log_file.txt | grep "WARNING" > warning_logs.txt
cat log_file.txt | grep "ERROR" > error_logs.txt
cat log_file.txt | grep "THREAT" > threats_log.txt
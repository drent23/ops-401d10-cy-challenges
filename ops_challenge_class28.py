#!/usr/bin/python3

# import modules
import logging

# Create logger
log = logging.getLogger('data_logger')

# Create handlers
# file handler and set level of msg to capture
file_handler = logging.FileHandler('file.log')
file_handler.setLevel(logging.WARNING)

# stream handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)

# Create formatters for handlers
file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# config formatters to apply to specific handler
file_handler.setFormatter(file_format)
stream_handler.setFormatter(stream_format)

# connect logger to handlers
log.addHandler(file_handler)
log.addHandler(stream_handler)



log.warning("This is a warning")
log.error("this is an error")


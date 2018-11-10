"""
Manage multiple loggers
"""

import logging
import sys


# logger 1: simply writes messages to text file
log1 = logging.getLogger('example1')
log1.addHandler(logging.FileHandler('logger1.log', mode='w'))
log1.setLevel(logging.INFO)
log1.info('message for logger 1')


# logger 2: formats timestamp and writes to standard error stream
log2 = logging.getLogger('example2')
handler = logging.StreamHandler(sys.stderr)
log2.addHandler(handler)
fmt='%(asctime)s | MY LOG MESSAGE IS: %(message)s'
handler.setFormatter(logging.Formatter(fmt, datefmt='%m/%d/%Y %I:%M:%S %p'))
log2.setLevel(logging.WARNING)
log2.warning('message for logger 2')

# level of logger 1 is still INFO
log1.info('another message for logger 1')

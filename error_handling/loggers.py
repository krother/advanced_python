import logging
import sys

# write log messages to text file and standard output
log = logging.getLogger('example logger')
log.setLevel(logging.INFO)

fmt='%(asctime)s | %(message)s'
format = logging.Formatter(fmt, datefmt='%m/%d/%Y %I:%M:%S %p')

handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(format)
log.addHandler(handler)

handler2 = logging.FileHandler('logfile.log', mode='w')
handler2.setFormatter(format)
log.addHandler(handler2)

log.info('message from logger ')
log.warning('message from logger 2')
log.error('an error has occured')

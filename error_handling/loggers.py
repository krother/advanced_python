import logging
import sys

# write log messages to text file and standard output
log = logging.getLogger('example logger')
log.setLevel(logging.INFO)

fmt='%(asctime)s | %(message)s'
formatter = logging.Formatter(fmt, datefmt='%m/%d/%Y %I:%M:%S %p')

handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(formatter)
log.addHandler(handler)

handler2 = logging.FileHandler('logfile.log', mode='w')
handler2.setFormatter(formatter)
log.addHandler(handler2)

log.info('message from logger ')
log.warning('message from logger 2')
log.error('an error has occured')

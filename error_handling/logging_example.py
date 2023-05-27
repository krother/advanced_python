
import logging


logging.basicConfig(filename='debug.log', level=logging.DEBUG)


def factorial(n=10):
    """Calculates factorials with log messages."""
    i = 1
    factorial = 1
    while i < n:
        logging.info('starting iteration {}'.format(i))
        factorial *= i
        logging.debug('new factorial: {}'.format(factorial))
        i += 1
    logging.warning('Final result: {}'.format(factorial))


if __name__ == '__main__':
    logging.warning('this is a warning message')
    factorial(10)
    logging.critical('Factorial calculation ended')



class Failsafe:
    '''
    Catches I/O errors.
    '''
    def __init__(self, func):
        self.function = func

    def __call__(self, *args):
        try:
            self.function(*args)
        except IOError:
            print('An I/O error was caught')
            print(args)

@Failsafe
def risky_fileopen(filename):
    open(filename)
    print('SUCCESS:', filename)


risky_fileopen('decorator_class.py')
risky_fileopen('doesnotexist')


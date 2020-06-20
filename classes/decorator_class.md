
# Decorator Classes

Decorator Classes are a structure to write more sophisticated decorators that have an internal state.
They allow you to pass arguments into the decorator as well.

Key points:

* the constructor `__init__()` receives the arguments given in the line starting with `@`
* the `__call__()` method should return the decorator function
* the `safe_call()` method gets called in the end (you can give it a different name)

Here is a code example that counts how many errors have been produced.

    :::python3
    class FailureCounter:

        def __init__(self, message):
            self.message = message
            self.function = None
            self.failcount = 0

        def __call__(self, func):
            self.function = func
            return self.safe_call

        def safe_call(self, *args):
            try:
                self.function(*args)
            except IOError:
                self.failcount += 1
                print(self.message)
                print(f'An I/O error was caught in {self.function.__name__}')
                print(f"with the file name '{args[0]}'")
                print(f'this is failure #{self.failcount}\n')

    @FailureCounter('--- FILE ERROR ---')
    def risky_fileopen(filename):
        open(filename)

    risky_fileopen('not_existing_file')
    risky_fileopen('doesnotexist_either')


'''
Write a decorator which wraps functions to log function arguments
and the return value on each call. 

Implement the 'logged' decorator so that the program produces
the following output:

you called func(4, 4, 4)
it returned 6
6

'''

@logged
def func(*args):
    return 3 + len(args)


print func(4, 4, 4)


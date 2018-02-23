"""
Function parameters

Discuss the calls of 'example' one by one
"""
def example(obligatory, optional=77, *args, **kwargs):
    print("obligatory: ", obligatory)
    print("optional  : ", optional)
    print("args      : ", args)
    print("kwargs    : ", kwargs)
    print()


example()
# example(True)
# example(True, 99)
# example(True, 99, 77)
# example(True, 99, 77, 55)
# example(True, 99, 77, 55, a=33, b=11)

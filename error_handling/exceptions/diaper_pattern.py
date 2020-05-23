"""
diaper pattern example

(This is how you should NOT build your try.. except clauses)
"""

def fibonacci(n):
    """Returns the n-th number from the Fibonacci series."""
    try:
        a = 0
        b = 1       
        while n > 0:
            temp = a+b
            a = b
            b = temp
            n -= 1
        return temp
    except:
        pass
        

examples = [1,3,0,7,10]
for number in examples:
    print(fibonacci(number))

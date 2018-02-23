
# Example: Mutable and immutable parameters.

def change(var1, var2):
    """Change two values."""
    var1 += [7]
    var2 += 7
    
    
data = [3,4,5]
number = 6

change(data, number)

print("The list now contains", data)
print("The number is now", number)



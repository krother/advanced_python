import sys

a = [1,2,3]
b = [a,a,4]
print(sys.getrefcount(a))

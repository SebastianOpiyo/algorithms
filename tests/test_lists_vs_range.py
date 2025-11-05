import sys
import time

range_size = range(10000)
list_size = list(range_size)

# Compare memory usage of the two structures
print (f"Memory size of range: {sys.getsizeof(range_size)} bytes") # Memory size of range: 48 bytes
print (f"Memory size of list: {sys.getsizeof(list_size)} bytes") # Memory size of list: 80056 bytes


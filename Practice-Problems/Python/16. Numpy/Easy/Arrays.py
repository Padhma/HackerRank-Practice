import numpy

def arrays(arr):
    return numpy.array(arr[::-1]).astype(numpy.float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
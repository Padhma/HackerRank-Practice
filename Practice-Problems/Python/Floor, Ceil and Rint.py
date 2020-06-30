import numpy as np
np.set_printoptions(sign=' ')
array = np.array(input().split(),float)
print(np.floor(array),np.ceil(array),np.rint(array),sep="\n")
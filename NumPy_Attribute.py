import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a.shape)
print(a.ndim)
print(a.itemsize)
x=np.empty([3,2],dtype=bytes)
print(x)
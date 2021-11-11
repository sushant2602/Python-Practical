import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
np.savetxt('test.txt',arr1)
arr=np.loadtxt('test.txt')
print(arr)
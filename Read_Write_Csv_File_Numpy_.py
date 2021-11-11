import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
np.savetxt('test.csv',arr1,delimiter=",")
arr=np.loadtxt('test.csv',delimiter=",")
print(arr)
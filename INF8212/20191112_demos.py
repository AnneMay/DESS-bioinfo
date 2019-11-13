from numpy import random, reshape, zeros, arange
from pprint import pprint

mat = zeros((3,3,3))
mat = random.random((2,2))
print(mat)
print(type(mat))
# ​
n = 2
mat1 = [[1.00 for k in range(n)] for j in range(n)]
print(type(mat1))
#print(mat1.reshape(4))
# ​
print(mat)
print(mat1)
# ​
# ​
# #print(mat1+mat)
mat2 = mat1*mat
print(type(mat2))
print(mat1@mat)
# ​
n=3
mat3 = [[[1 for k in range(n)] for j in range(n)] for i in range(n)]
pprint(mat3)
# ​
mat4 = arange(16)
# print(mat4)
print(mat4.reshape(4,4))



mat5 = arange(11, 100, 11).reshape(3,3)
# print(mat5)
# print(mat5.reshape(3,3))
print(mat5[:,2])
mat5[mat5 %2 == 0] = -1
print(mat5)
# ​
# """
# #Pour exercice
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris = np.genfromtxt(url, delimiter=',', dtype='float',usecols=[0])
# """

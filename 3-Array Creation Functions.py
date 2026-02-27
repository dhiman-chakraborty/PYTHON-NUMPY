import numpy as np

# Zeros Array → np.zeros(): Creates an array filled with 0s

arr1 = np.zeros(5)      # 1D → [0. 0. 0. 0. 0.]
arr2 = np.zeros((2,4))     # 2D → 2x3 matrix with all zeros(rows,columns)
arr3 = np.zeros((2,2,3))      # Create a 3D array of shape (2, 3, 4) → 2 blocks, 3 rows, 4 columns    

print(arr1,'\n')
print(arr2,'\n')
print(arr3,'\n')


# Ones Array → np.ones(): Creates an array filled with 1s
a = np.ones(5)
b = np.ones((2,3))
c = np.ones((2,2,3))

print(a)
print(b)
print(c)
print(a.dtype)


# Identity Matrix → np.eye(): Creates a square matrix with 1s on the diagonal

a1 = np.eye(2)        # eye() → Square or Rectangular (N × M)
a2 = np.eye(2,4)
a3 = np.identity(5)        # identity() → Only Square (N × N)

print(a1)
print(a2)
print(a3)


# Diagonal Matrix → np.diag(): Creates a diagonal array from a given list
arr_diag1 = np.diag([1,2,3])
arr_diag2 = np.diag([1,2,3,5])
print(arr_diag1)
print(arr_diag2)

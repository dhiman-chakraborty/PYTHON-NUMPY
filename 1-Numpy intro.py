import numpy as np

# Creating Arrays

# Creating Array from list - 1D Array
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))

# Creating Array from tuple - 1D Array
arr2 = np.array((1,2,3,4,5,6))
print(arr2)
print(type(arr2))

# Multi-dimensional - 2D Array (Matrix)
arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3)
print(type(arr3))

# 3D Array - 3D array is not a matrix, it's collection of Matrices
arr4 = np.array([[[1,2,3],[4,5,6]],[[6,8,9],[6,5,6]],[[4,6,4],[4,8,6]]])
print(arr4)
print(type(arr4))
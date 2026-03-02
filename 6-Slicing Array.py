import numpy as np

# Slicing Array
# Extract multiple elements using [start:end:step] (just like Python lists).

# start = starting index (included)
# end = ending index (excluded)
# step = jump size

# Slicing in 1D Arrays
# a = np.array([10,20,30,40,50,60])

# print(a[1:4])   # from index 1 to 3
# print(a[1:])    # from index 1 to end
# print(a[:4])    # from start to index 3
# print(a[::2])   # step = 2
# print(a[1:5:2])   # start=1, end=5, step=2
# print(a[::-1])    # Reverse array


# Slicing in 2D Arrays

# Syntax: arr[row_start:row_end , col_start:col_end]

# arr2 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

# print(arr2[1,0:2])      # row: 2, col: 1-2
# print(arr2[1:3,1:3])    # row: 2-3, col: 2-3
# print(arr2[0,1])        # row: 1, col:2
# print(arr2[:,1])        # row: all, col:2
# print(arr2[2,:])        # row: 2,col: all
# print(arr2[::2,::2])    # every 2nd row & every 2nd col


# Slicing in 3D Arrays

# Syntax: arr[depth_start:depth_end, row_start:row_end, col_start:col_end]
arr3 = np.array([[[ 1,  2,  3],[ 4,  5,  6]],[[ 7,  8,  9],[10, 11, 12]]])

print(arr3[0,1,1:3])      # depth: 1, row: 2, coloum: 2-3
print(arr3[:,1,1:3])      # depth: all, row: 2, coloum: 2-3
print(arr3[:,:,0:2])      # depth: all, row: all, col: 1-2
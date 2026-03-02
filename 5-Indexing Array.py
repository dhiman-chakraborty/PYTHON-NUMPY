import numpy as np

# Note: indices always start at 0

a = np.array([10,20,30,40,50])

print(a[2])    # 3rd element
print(a[-2])     # 2nd last element
print(a[::-1])     # Reverse array

# Index with List/Array
print(a[[0,2,3]])


# 2D Array

# Syntax: arr[row, column]

arr2 = np.array([[1, 2, 3],[4, 5, 6]])
print(arr2[0,1])    # row-1,column-2
print(arr2[1,1])     # row-2,column-2
print(arr2[-1,-2])     #last row,2nd last column


# 3D Array

# Syntax: arr[depth, row, column]
b = np.array([[[1, 2], [3, 4]],[[5, 6], [7, 8]]])

print(b[1,1,0])    # 2nd bolck,2nd row,1st column
print(b[0,0,1])    # 1st block,1st row,2nd column


# Boolean Indexing
c = np.array([10,52,6,41,13,25,9,24])

print(c[c>25])
print(c[c%2==0])
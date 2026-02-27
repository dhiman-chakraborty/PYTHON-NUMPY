import numpy as np

# NumPy Array Attributes

# Number of Dimensions(ndim --> Number of Dimension)
arr1 = np.array([1,2,3,4,5])    # 1D
arr2 = np.array([[1,2,3],[4,5,6]])     # 2D
arr3 = np.array([[[1,3,6],[4,5,6]],[[4,6,4],[7,8,9]]])     #3D
arr4 = np.array([[[1,3,6],[4,5,6]],[[4,6,4],[7,8,9]],[[4,5,6],[7,8,9]]]) 

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# Shape(depth,rows,column)
print(arr1.shape)
print(arr2.shape)
print(arr3.shape)
print(arr4.shape)

# Size(Total number elements)
print(arr1.size)
print(arr2.size)
print(arr3.size)
print(arr4.size)


# Type of array(dtype → Data Type of Elements)

arr_num = np.array([1,2,3,4,5])
arr_float = np.array([2.5,6.4,1.3,4.7])
arr_numfloat = np.array([4,5.6,3,2.1,7])
arr_str = np.array(["a","b","c","d"])
arr_mixed = np.array([1,"a","b",6,"k",8])

print(arr_num.dtype)
print(arr_float.dtype)
print(arr_numfloat.dtype)
print(arr_str.dtype)
print(arr_mixed.dtype)


# itemsize → Size of Each Element in Bytes
arrint = np.array([1,2,3])     # 8 bytes(each int)
arrfloat = np.array([5.3,6.3,4.5])    # 8 bytes(each float)

print(arrint.itemsize)
print(arrfloat.itemsize)


# T --> Transpose of Array
arr_t = np.array([[1,2,3],[4,5,6]])
print(arr_t)
print(arr_t.T)


# flat → Iterator Over Element
arrr = np.array([[1,2,3],[5,6,6]])
print(arrr,'\n')
print(list(arrr.flat),'\n')

for i in arrr.flat:
    print(i)
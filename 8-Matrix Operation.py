import numpy as np

# Matrix Addition & Subtraction
# Performed element-wise.
# Matrices must have the same shape.
a1 = np.array([[1,2],[3,4]])
a2 = np.array([[5,6],[4,3]])

print("Addition :", a1 + a2)
print("Subtraction :", a2 - a1)

# Matrix Multiplication
print("Multiplication:", a1 * a2)


# Matrix Multiplication (@ or np.dot)
print("Matrix Multiplication :\n", a1 @ a2)      
print("Matrix Multiplication :\n", np.dot(a1,a2))
print("Matrix Multiplication :\n", a1.dot(a2))


# Scalar Multiplication & Division
# Multiply / divide every element by a scalar.
a3 = np.array([[5,6],[3,7]])

print("Scalar Multiplication :\n", a3 * 2)
print("Scalar Division :\n", a3 / 2)


# Transpose of a Matrix
# Rows become columns, columns become rows.
a4 = np.array([[1,2,3],[5,6,7]])

print("Transpose :\n", a4.T)
print("Transpose :\n", np.transpose(a4))         # Using np.transpose()


# Inverse of a Matrix
# Square matrices only, determinant ≠ 0
a5 = np.array([[5,6],[7,8]])
print("Inverse :\n",np.linalg.inv(a5))


# Determinant of a Matrix
# Square matrices only.
print("Determinant :",np.linalg.det(a5))
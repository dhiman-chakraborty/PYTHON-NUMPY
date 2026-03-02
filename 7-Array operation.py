import numpy  as np

# Arithmetic Operations

# Element-wise operations on arrays of the same shape.
a = np.array([10,20,30])
b = np.array([5,6,7])

print("a + b :",a + b)
print("a - b:",a - b)
print("a * b:",a * b)
print("a / b:",a / b)


# Arithmetic Scalar Operations

# Scalar operations mean performing mathematical or logical operations between 
# a NumPy array and a single number (scalar). The scalar is applied element-wise to all elements of the array.

c = np.array([10,20,30,40,50,60,70])

print(c + 10)
print(c - 5)
print(c * 3)
print(c / 5)
print(c ** 2)


# Comparison Operations

# Comparison operations are used to compare each element of a NumPy array with either:

# A scalar (number)
# Another array (of the same shape or broadcastable shape)
# They return a Boolean array (True / False).

# Array vs Scalar
d = np.array([50,55,41,32,86])

print(d > 25)
print(d < 60)
print(d == 55)
print(d != 41)

# Array vs Array (element-wise comparison)
a1 = np.array([15,23,6])
a2 = np.array([12,31,7])

print(a1 > a2)
print(a1 < a2)
print(a1 == a2)

# Chained Comparisons
b1 = np.array([50,6,3,7,12,31])

print((b1 >=10) & (b1 <=30))
print((b1 >=10) | (b1 <=30))
print(~(b1 >=10))


# Functions for Comparison

# NumPy also provides special functions:

# np.greater(a, b) → a > b
# np.less(a, b) → a < b
# np.equal(a, b) → a == b
# np.not_equal(a, b) → a != b
# np.greater_equal(a, b) → a >= b
# np.less_equal(a, b) → a <= b

a3 = np.array([10,6,45])
a4 = np.array([6,12,3])

print(np.greater(a3,a4))
print(np.not_equal(a3,a4))                  
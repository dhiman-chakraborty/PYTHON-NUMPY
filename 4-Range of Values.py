import numpy as np

# Range of Values → np.arange(): Like Python’s range(), but returns a NumPy array

# Syntax: numpy.arange([start,] stop[, step], dtype=None)
a = np.arange(5)
b = np.arange(2,10,2)
c = np.arange(2,10)

print(a)
print(b)
print(c)


# Evenly Spaced Values → np.linspace(): Generates numbers between two values with equal spacing
d = np.linspace(1,10,6)
print(d)

# Random Arrays: NumPy has multiple random array generators
# Random values between 0 and 1
# Syntax: numpy.random.rand(d0, d1, ..., dn)   --> d0, d1, d2,.... for dimention
e = np.random.rand(3,4)
print(e)


# Random integers
# Syntax: numpy.random.randint(low, high=None, size=None, dtype=int) 
        # low:	The lowest (inclusive) integer to be drawn. (optional)
        # high	The highest (exclusive) integer to be drawn.
        # size	Shape of the output array (e.g. (2, 3) for 2×3). If None, returns a single integer.
        # dtype	The desired data type of the output (default = int).
a1 = np.random.randint(5)
a2 = np.random.randint(2,10,size=5)       #  a2 = np.random.randint(2,10,5)
a3 = np.random.randint(4,10,size=(2,3))      # a3 = np.random.randint(4,10,(2,3))  

print(a1)
print(a2)
print(a3)


# Full Array → np.full(): Creates an array filled with a specific value

# Syntax: numpy.full(shape, fill_value)
b1 = np.full((2,4),6)
b2 = np.full(6,8)

print(b1)
print(b2)
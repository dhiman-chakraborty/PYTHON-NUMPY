import numpy as np

# Broadcasting
# Broadcasting is NumPy’s way of handling arithmetic operations between arrays of different shapes.
# Instead of throwing an error, NumPy tries to stretch (broadcast) the smaller array to match the shape of the larger one.
 

# Broadcasting Rules: When operating on two arrays, NumPy compares their shapes element-wise (from right to left):

# If the dimensions are equal → ✅ okay.
# If one of the dimensions is 1 → it can be stretched (broadcast).
# If dimensions don’t match and none is 1 → ❌ error.

# Simple Example: Add a scalar to an array
a = np.array([4,6,3])

print("+5 :",a + 5)    # a + 5 -->[4,6,3]+[5,5,5]-->[9 11 8]


# Example: Adding 1D array to 2D array
a1 = np.array([[5,9,3],
               [7,6,3]])
a2 = np.array([10,20,30])
# a3= np.array([10,20])      # Broadcasting not possible
print("sum:\n",a1 + a2)


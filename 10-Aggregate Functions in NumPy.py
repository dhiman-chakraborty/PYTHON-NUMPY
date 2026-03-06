import numpy as np

# Aggregate Functions in NumPy

# Function	        Description	                  Example
# np.sum()	        Sum of elements	              np.sum(arr)
# np.mean()	        Mean (average)	              np.mean(arr)
# np.median()	    Median value	              np.median(arr)
# np.min()	        Minimum element	              np.min(arr)
# np.max()	        Maximum element	              np.max(arr)
# np.std()	        Standard Deviation	          np.std(arr)
# np.var()	        Variance	                  np.var(arr)
# np.prod()	        Product of elements	          np.prod(arr)
# np.cumsum()	   Cumulative sum	              np.cumsum(arr)
# np.cumprod()	   Cumulative product	          np.cumprod(arr)
# np.argmin()	   index of the minimum element	  np.argmin(arr)
# np.argmax()	   index of the maximum element	  np.argmax(arr)
# np.sqrt()	       square root of each element	  np.sqrt(arr)
# np.exp()	       exponential of each element	  np.exp(arr)


# Example with 1D Array
a = np.array([4,6,3,7,9,10])

print("Sum :",np.sum(a))
print("Mean :",np.mean(a))
print("Median :",np.median(a))
print("Min :",np.min(a))
print("Max :",np.max(a))
print("Product :",np.prod(a))
print("Std :",np.std(a))
print("Variance :",np.var(a))

# `Example with 2D Array (axis parameter)`
b = np.array([[14,26,137,25],
              [40,63,78,21]])


print("Sum :",np.sum(b))
print("Sum(Axis=0) :",np.sum(b,axis=0))       # axis=0 -->(column-wise sum)
print("Sum(Axis=1) :",np.sum(b,axis=1))       # axis=1 -->(row-wise sum)
print("Min :",np.min(b))
print("Min(Axis=0):",np.min(b,axis=0))
print("Min(Axis=1):",np.min(b,axis=1))
print("Mean(Axis=0):",np.mean(b,axis=0))
print("Mean(Axis=1):",np.mean(b,axis=1))


# Cumulative Aggregates
print("Cumulative aggregate:",np.cumulative_sum(a))
print("Cumulative Product:",np.cumulative_prod(a))

# Aggregate Logical Functions
arr = np.array([True, False, True])

print("All True?", np.all(arr))   # False
print("Any True?", np.any(arr))   # True
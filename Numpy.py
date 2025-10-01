NumPy Basics Tutorial
NumPy is a powerful library for numerical computing.

Arrays are central: multidimensional, fast, and flexible.

You can create arrays in many ways.

Perform fast element-wise operations.

Use slicing, reshaping, stacking.

Take advantage of broadcasting and aggregation functions.




                           
1. Operations on an Array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Basic arithmetic
print(arr + 5)       # Add 5 to each element
print(arr * 2)       # Multiply each element by 2
print(arr - 1)       # Subtract 1 from each element
print(arr / 2)       # Divide each element by 2
print(arr ** 2)      # Square each element


Output:

[ 6  7  8  9 10]
[ 2  4  6  8 10]
[0 1 2 3 4]
[0.5 1.  1.5 2.  2.5]
[ 1  4  9 16 25]

2. Reading Elements of an Array
arr = np.array([[10, 20, 30], [40, 50, 60]])

print(arr[0, 1])    # Element at first row, second column
print(arr[1])       # Entire second row
print(arr[:, 2])    # All rows, third column


Output:

20
[40 50 60]
[30 60]

3. Replace Elements in an Array
arr = np.array([1, 2, 3, 4, 5])

arr[arr > 3] = 10   # Replace all elements greater than 3 with 10
print(arr)


Output:

[ 1  2  3 10 10]

4. Missing Values in an Array

Note: NumPy arrays of integer type cannot hold NaN values, so typically use float arrays for missing values.

arr = np.array([1, 2, np.nan, 4, 5])
print(np.isnan(arr))  # Check for NaNs
print(arr[np.isnan(arr)])  # Extract NaNs


Output:

[False False  True False False]
[nan]

5. Stack Arrays Vertically
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

v_stacked = np.vstack((a, b))
print(v_stacked)


Output:

[[1 2 3]
 [4 5 6]]

6. Stack Arrays Horizontally
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

h_stacked = np.hstack((a, b))
print(h_stacked)


Output:

[1 2 3 4 5 6]

7. Common Items Between Two Arrays
a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5, 6])

common = np.intersect1d(a, b)
print(common)


Output:

[3 4]

8. Remove Common Elements
a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5, 6])

result = np.setdiff1d(a, b)  # Elements in a not in b
print(result)


Output:

[1 2]

9. Process Elements on Conditions

Example: square all even numbers

arr = np.array([1, 2, 3, 4, 5, 6])

arr[arr % 2 == 0] = arr[arr % 2 == 0] ** 2
print(arr)


Output:

[ 1  4  3 16  5 36]

10. Check for Elements in an Array Using isin()
arr = np.array([1, 2, 3, 4, 5])
check = [2, 5, 7]

mask = np.isin(arr, check)
print(mask)          # Boolean mask
print(arr[mask])     # Elements present in check


Output:

[False  True False False  True]
[2 5]

11. Reverse Array
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print(reversed_arr)


Output:

[5 4 3 2 1]

12. Sorting Array
arr = np.array([3, 1, 4, 5, 2])
sorted_arr = np.sort(arr)
print(sorted_arr)


Output:

[1 2 3 4 5]

13. "N" Largest & Smallest Numbers in an Array
arr = np.array([10, 50, 20, 40, 30])

n = 3
smallest_n = np.partition(arr, n-1)[:n]  # 3 smallest
largest_n = np.partition(arr, -n)[-n:]  # 3 largest

print("Smallest:", smallest_n)
print("Largest:", largest_n)


Output: (order in smallest/largest may vary)

Smallest: [10 20 30]
Largest: [30 40 50]

14. Repeating Sequences
arr = np.array([1, 2, 3])
repeated = np.tile(arr, 3)      # Repeat whole array 3 times
print(repeated)

repeated_elements = np.repeat(arr, 2)  # Repeat each element 2 times
print(repeated_elements)


Output:

[1 2 3 1 2 3 1 2 3]
[1 1 2 2 3 3]

15. Compare Arrays
a = np.array([1, 2, 3])
b = np.array([1, 4, 3])

equal = a == b
print(equal)                # Element-wise comparison

all_equal = np.array_equal(a, b)
print(all_equal)            # Check if all elements are equal


Output:

[ True False  True]
False

 1. Frequent Values in an Array

To find the most frequent (mode) values in an array:

from scipy import stats
import numpy as np

arr = np.array([1, 2, 2, 3, 4, 4, 4, 5])
mode = stats.mode(arr)
print("Most frequent value:", mode.mode[0])
print("Frequency count:", mode.count[0])


Output:

Most frequent value: 4
Frequency count: 3

2. Read-Only Array

You can create a read-only (immutable) array using the flags.writeable attribute.

arr = np.array([1, 2, 3, 4, 5])
arr.flags.writeable = False  # Make it read-only

try:
    arr[0] = 10
except ValueError as e:
    print("Error:", e)


Output:

Error: assignment destination is read-only

3. Load & Save Arrays

To save and load arrays to/from files:

arr = np.array([1, 2, 3, 4, 5])

# Save to a file
np.save('my_array.npy', arr)

# Load from the file
loaded_arr = np.load('my_array.npy')
print(loaded_arr)


Output:

[1 2 3 4 5]

4. Printing Options

You can set printing options for NumPy arrays to control how they are displayed.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Set precision and suppress scientific notation
np.set_printoptions(precision=2, suppress=True)
print(arr)


Output:

[ 1  2  3  4  5  6  7  8  9 10]

5. Vector Addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = a + b  # Element-wise addition
print(result)


Output:

[5 7 9]

6. Multiplication of Vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = a * b  # Element-wise multiplication
print(result)


Output:

[ 4 10 18]

7. Dot Product

The dot product of two vectors is computed as the sum of the element-wise products.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)
print(dot_product)


Output:

32

8. Length of a Vector

The length (or magnitude) of a vector is the square root of the sum of the squares of its components.

a = np.array([3, 4])

length = np.linalg.norm(a)
print("Length of vector:", length)


Output:

Length of vector: 5.0

9. Normalized Vector

To normalize a vector, we divide each element by the vector's length:

a = np.array([3, 4])

# Normalizing the vector
normalized = a / np.linalg.norm(a)
print("Normalized vector:", normalized)


Output:

Normalized vector: [0.6 0.8]

10. Angle Between Vectors

The angle between two vectors can be calculated using the dot product formula:

cos
⁡
(
𝜃
)
=
𝑎
⋅
𝑏
∥
𝑎
∥
∥
𝑏
∥
cos(θ)=
∥a∥∥b∥
a⋅b
	​


Where 
𝜃
θ is the angle between vectors a and b.

a = np.array([1, 0])
b = np.array([0, 1])

# Dot product
dot_product = np.dot(a, b)

# Magnitudes (lengths) of the vectors
mag_a = np.linalg.norm(a)
mag_b = np.linalg.norm(b)

# Cosine of the angle
cos_theta = dot_product / (mag_a * mag_b)

# Angle in radians
theta_radians = np.arccos(cos_theta)

# Convert to degrees
theta_degrees = np.degrees(theta_radians)

print(f"Angle between vectors: {theta_degrees} degrees")


Output:

Angle between vectors: 90.0 degrees

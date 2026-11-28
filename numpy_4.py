import numpy as np

# Create two 2x3 matrices (2D arrays)
matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6]])

matrix_b = np.array([[7, 8, 9],
                     [10, 11, 12]])

# Perform matrix addition
result = matrix_a + matrix_b

print("Matrix A:\n", matrix_a)
print("\nMatrix B:\n", matrix_b)
print("\nSum of Matrices:\n", result)

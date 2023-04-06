import numpy as np

# Define the system of equations
A = np.array([[25, 5, 1], [64, -8, 1], [144, 12, 1]])
b = np.array([106.8, 177.2, 279.2])

# Define the initial guess
x0 = np.array([0, 0, 0])

# Define the maximum number of iterations
max_iter = 1000

# Define the tolerance
tol = 1e-10

# Define the Gauss-Seidel method function
def gauss_seidel(A, b, x0, max_iter, tol):
    n = len(x0)
    x = x0.copy()
    for k in range(max_iter):
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x0[i+1:])) / A[i, i]
        if np.linalg.norm(x - x0) < tol:
            return x
        x0 = x.copy()
    return x

# Call the Gauss-Seidel method function
x = gauss_seidel(A, b, x0, max_iter, tol)
# Print the solution
print(x)
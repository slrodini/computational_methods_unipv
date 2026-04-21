import numpy as np

A = np.array([[-21, 19, -20], [19, -21, 20], [40, -40, -40]])

B = np.identity(3) + 0.1 * A
C = np.identity(3) + 0.001 * A

eigenvalues, eigenvectors = np.linalg.eig(B)

print("Eigenvalues:")
print(eigenvalues)

print(np.pow(B, 100).dot(np.array([1, 0, -1])))
print(np.pow(C, 100).dot(np.array([1, 0, -1])))

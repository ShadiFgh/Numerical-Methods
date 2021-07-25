import numpy as np
import pprint
from math import sqrt

n = int(input("Please enter the number of rows of the matrix:"))

matrix = []
print("Please enter the matrix's components\nExample:\n1\n2\n3\n4\nplease enter here")

for i in range(n):
    a = []
    for j in range(n):
        a.append(float(input()))
    matrix.append(a)

print("Your matrix is:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end="  ")
    print()

b = []
print('Please enter the elements of vector b:')
for i in range(n):
    b.append(float(input()))


def IsPositiveDefinite(x):
    return np.all(np.linalg.eigvals(x) > 0)

if IsPositiveDefinite(matrix) == True:
    print('This matrix is positive definite.')
else:
    print('This matrix is not positie definie.')


def LU_decomposition(A):

    n = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    for j in range(n):
        L[j][j] = 1.0

        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A[i][j] - s1

        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (A[i][j] - s2) / U[j][j]

    return (L, U)
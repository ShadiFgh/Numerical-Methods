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


def cholesky(A):

    n = len(A)
    R = [[0.0] * n for i in range(n)]

    for i in range(n):
        for k in range(i + 1):
            z = sum(R[i][j] * R[k][j] for j in range(k))

            if (i == k):
                R[i][k] = sqrt(A[i][i] - z)
            else:
                R[i][k] = (1.0 / R[k][k] * (A[i][k] - z))
    return R


def ForwardAndBackSub(L, U, b):

    n = len(L)
    x = np.zeros((n), float)
    y = np.zeros((n), float)
    for i in range(0, n):
        s = b[i]
        for j in range(0, i):
            s = s - L[i][j] * y[j]
        y[i] = s

    for i in range(n - 1, -1, -1):
        s = y[i]
        for j in range(i + 1, n):
            s = s - U[i][j] * x[j]
        x[i] = s / U[i][i]
    return x
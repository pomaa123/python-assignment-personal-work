'''
practising Numpy
'''

##creating a vector
import numpy as np
from numpy import array
from numpy import tril
from numpy import triu
from numpy import diag
from numpy import identity
from numpy.linalg import inv

a = array([1, 2, 3])
print(a)

b = array([2, 4, 6])
print(b)

#checking the data type
print(a.dtype)

#checking the shape of the vector/matrix
print(a.shape)

# vector addition
c = a + b
print(c)
#vector subtraction
d = a - b
print(d)
#vector multiplication
e = a * b
print(e)

##vector division
f = a/b
print(f)

##dot-product of vectors
g = b.dot(a)
print(g)

#vector scalar multiplication
one = array([1,4,3,2])
s = 5
c = s*one
print(c)

##vector L1 norm
from numpy.linalg import norm
a_1 = array([2,3,5,4])
L_1 = norm(a_1, 1)
print(L_1)

##Euclidean norm
l_2 = norm(a_1)
print(l_2)
print(maxnorm)
from math import inf
maxnorm = norm(a_1, inf)

##creating a matrix
A = array([[1, 2, 3], [4, 5, 6]])
print(A)
w = A[1,0]
print(w)

B = array([[3, 5, 7], [1, 4, 6]])
print(B)

## matrix aritmetic
C = A + B
print(C)
D =A - B
print(D)
E = A * B
print(E)
F = A/B
print(F)
## matrix - matrix multiplication
A_1 = array([[2,1,1],[3,2,1],[4,0,0]])
B_1 = array([[1,0,0],[0,1,0],[0,0,1]])

G = A_1.dot(B_1)
print(G)
#vector-matrix multiplication
#given a vector,
v = array([2,1,2])
X = A_1.dot(v)
print(X)

##types of matrix


#define a square matrix
matrix_a = array([[2,2,4],[1,0,1],[3,2,1]])
print(matrix_a)

lower = tril(matrix_a)
print(lower)

upper = triu(matrix_a)
print(upper)

diagonal = diag(matrix_a)
print(diagonal)
D = diag(diagonal)
print(D)

identity_matirx = identity(3)
print(identity_matirx)

Q = array([[1,0],[0,-1]])
V = inv(Q)
print(V)
print(Q.T)

## inverse of Q x transpose of Q will give an identity matrix
I = Q.dot(Q.T)
print(I)

##matrix operations
#to cal. transpose,
Trans = Q.T
print(Trans)

##inverse matrix
A_2 = array([[1.0,2.0],[3.0,4.0]])
print(A_2)
B_2 = inv(A_2)
print(B_2)
I = A_2.dot(B_2)
print(I)
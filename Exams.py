import numpy as np
from numpy import array



def linear_equation():
    A = array([[20, 15,10, 45],[-3, -2.249, 7, 1.751],[5, 1, 3, 9]])

    row_2 = A[1] + (3/20)*A[0]
    print(row_2)

    row_3 = A[2] - (5/20)*A[0]
    print(row_3)
    ## Assigning the new row 2 and row 3 to the matrix A
    A[1] = row_2
    #print(A[1])
    A[2] = row_3
    # print(A[2])
    # print(A)
    second_row_3 = A[2] + (2.75/0.001)*A[1]
    print(second_row_3)
    A[2] = second_row_3
    print(A)

    x3 = A[2,3]/A[2,2]
    print(x3)

    x2 = (A[1,3]- A[1,2]*x3 )/A[1,1]
    print(x2)

    x1 = (A[0,3]- A[0,1]*x2 - A[0,2]*x3)/A[0,0]
    print(x1)

linear_equation()


def guassian_elimination():
    MatA = [[10,15,20,45],[-3,-2.249, 7, 1.751],[5, 1, 3, 9]]
    r1 = []
    for i in range(len(MatA[1])):
        r1.append(MatA[1][i] - (MatA[1][0]/MatA[0][0])*MatA[0][i])
    print(r1)

    r2 = []
    for i in range(len(MatA[2])):
        r2.append(MatA[2][i] - MatA[2][0]/MatA[0][0]*MatA[0][i])
    print(r2)

    MatA[1] = r1
    MatA[2] = r2
    

    second_r2 = []
    for j in range(len(MatA[2])):
        second_r2.append(MatA[2][j] - (MatA[2][1]/MatA[1][1])*MatA[1][j])
    print(second_r2)
    MatA[2] = second_r2
    print(MatA)

    x3 = MatA[2][2]/MatA[2][3]
    print(x3)

    x2 = (MatA[1][3] - MatA[1][2]*x3)/MatA[1][1]
    print(x2)
    
    x1 = (MatA[0][3] - MatA[0][1]*x2 - MatA[0][2]*x3)/MatA[0][0]
    print(x1)
guassian_elimination()    

A_1 = np.array([[20, 15,10],[-3, -2.249, 7],[5, 1, 3]])
A_2 = np.array([45 , 1.751, 9])
Matrix = np.linalg.solve(A_1, A_2)
print(Matrix)
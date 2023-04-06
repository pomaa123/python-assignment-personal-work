import numpy as np

matA = [[25,5,1], [64,8,1], [144,12,1]]

def lu_decomposition(matrix):

    mult_1 = matrix[1][0]/matrix[0][0]
    print(mult_1)
    row_2 = []
    for element_1 in range(len(matrix[1])):
        row_2.append(matrix[1][element_1] - (mult_1) * matrix[0][element_1])
    #print(row_2)

    mult_2 = matrix[2][0]/matrix[0][0] 
    print(mult_2)   
    row_3 = []
    for elements in range(len(matrix[2])):
        row_3.append(matrix[2][elements] - (mult_2)*matrix[0][elements])
    #print(row_3)

    matrix[1] = row_2
    matrix[2] = row_3

        #print(matrix)
        # R3 = R3 - (21/26)R2
    mult_3 = matrix[2][1]/matrix[1][1]
    print(mult_3)
    second_row_3 = []
    for element in range(len(matrix[2])):
        second_row_3.append(matrix[2][element] - (mult_3) * matrix[1][element])
    #print(second_row_3)

    matrix[2] = second_row_3
    print(matrix)

    lower_triangular = [[1,0,0], [0,1,0], [0,0,1]]
    lower_triangular[1][0] = mult_1
    lower_triangular[2][0] = mult_2
    lower_triangular[2][1] = mult_3

    print(lower_triangular)
    
    l = np.array(lower_triangular)
    U = np.array(matrix)
    lu = l.dot(U)
    print(lu)


lu_decomposition(matA)
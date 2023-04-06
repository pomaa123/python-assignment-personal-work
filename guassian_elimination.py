

matA = [[25,5,1], [64,8,1], [144,12,1]]

def gauss_elim(matrix):
    
    # R2 = R2 - (64/25) *R1
    row_2 = []
    for element_1 in range(len(matrix[1])):
        row_2.append(matrix[1][element_1] - (matrix[1][0]/matrix[0][0]) * matrix[0][element_1])
    print(row_2)

    
    row_3 = []
    for elements in range(len(matrix[2])):
        row_3.append(matrix[2][elements] - (matrix[2][0]/matrix[0][0])*matrix[0][elements])
    print(row_3)

    matrix[1] = row_2
    matrix[2] = row_3

    #print(matrix)
    # R3 = R3 - (21/26)R2
    second_row_3 = []
    for element in range(len(matrix[2])):
        second_row_3.append(matrix[2][element] - (matrix[2][1]/matrix[1][1]) * matrix[1][element])
    print(second_row_3)

    matrix[2] = second_row_3
    print(matrix)


gauss_elim(matA)




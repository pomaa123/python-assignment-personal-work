matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# create an empty matrix for the transpose
transpose = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

# iterate through rows of matrix
for i in range(len(matrix)):
    # iterate through columns of matrix
    for j in range(len(matrix[0])):
        # assign element at i,j to transpose at j,i
        transpose[j][i] = matrix[i][j]

# print the transpose
for row in transpose:
    print(row)
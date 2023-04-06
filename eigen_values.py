def find_eigen(matrix):
    # calculate the determinant of the matrix
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # calculate the trace of the matrix
    trace = matrix[0][0] + matrix[1][1]

    # calculate the eigenvalues
    lambda1 = (trace + ((trace ** 2) - (4 * det)) ** 0.5) / 2
    lambda2 = (trace - ((trace ** 2) - (4 * det)) ** 0.5) / 2

    # calculate the eigenvectors
    vector1 = [matrix[0][1], lambda1 - matrix[0][0]]
    vector2 = [matrix[0][1], lambda2 - matrix[0][0]]

    # normalize the eigenvectors
    norm1 = (vector1[0] ** 2 + vector1[1] ** 2) ** 0.5
    norm2 = (vector2[0] ** 2 + vector2[1] ** 2) ** 0.5

    vector1[0] /= norm1
    vector1[1] /= norm1

    vector2[0] /= norm2
    vector2[1] /= norm2

    return (lambda1, vector1), (lambda2, vector2)

# example usage
matrix = [[2, -1], [4, 3]]
eigenvalues, eigenvectors = find_eigen(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
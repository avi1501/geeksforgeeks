def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            martix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]


def printMatrix(matrix):
    for row in matrix:
        print(row)

def reverseColumns(matrix):
    for i in range(len(matrix)):
        j = 0
        k = len(matrix)-1
        while j<k :
            matrix[j][i],matrix[k][i] = matrix[k][i],matrix[j][i]
            j += 1
            k -= 1
'''
rotating a matrix by 90 degree using extra space

'''




def rotatematrixusingextraspace(matrix):
    m = len(matrix)
    n = len(matrix[0])
    resultant_matrix=[]
    for i in range(n):
        resultant_matrix.append([0]*m)

    for i in range(m):
        for j in range(n):
            resultant_matrix[n-j-1][i] = matrix[i][j]

    return resultant_matrix

def printMatrix(matrix):
    for rows in matrix:
        print(rows)

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],  
          [9, 10, 11, 12],
          [9, 10, 11, 12],
          
         ] 
matrix = rotatematrixusingextraspace(matrix)

printMatrix(matrix)

    
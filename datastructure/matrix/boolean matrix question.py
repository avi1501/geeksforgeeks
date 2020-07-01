def boolmatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row = [0]*m
    col = [0]*n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                row[i] = 1
                col[j] = 1
    for i in range(m):
        for j in range(n):
            if col[j] == 1 or row[i] == 1:
                matrix[i][j] = 1
            
def printMatrix(matrix):
    for rows in matrix:
        print(rows)

matrix = [
            [1,0,0,1],
            [0,0,1,0],
            [0,0,0,0],
            [0,0,0,0]
         ]

print('matrix before')
printMatrix(matrix)
boolmatrix(matrix)
print('matrix after')
printMatrix(matrix)

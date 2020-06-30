def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

def printMatrix(matrix):
    for rows in matrix:
        print(rows)

arr = [[1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12], 
        [13, 14, 15, 16] 
    ]

printMatrix(arr)
transpose(arr)

print("---------------------")
print("---------------------")

printMatrix(arr)


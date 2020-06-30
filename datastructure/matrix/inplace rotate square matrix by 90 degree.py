def inplacematrixrotation(matrix):
    for x in range(0,len(matrix)//2):
        for y in range(x,len(matrix)-x-1):
            temp = matrix[x][y]

            matrix[x][y] = matrix[y][len(matrix)-x-1]

            matrix[y][len(matrix)-x-1] = matrix[len(matrix)-x-1][len(matrix)-y-1]

            matrix[len(matrix)-x-1][len(matrix)-y-1] = matrix[len(matrix)-y-1][x]

            matrix[len(matrix)-y-1][x] = temp

def printMatrix(matrix):
    for row in matrix:
        print(row)

matrix = [ [1, 2, 3, 4 ], 
        [5, 6, 7, 8 ], 
        [9, 10, 11, 12 ], 
        [13, 14, 15, 16 ] ] 

inplacematrixrotation(matrix)

printMatrix(matrix)
          
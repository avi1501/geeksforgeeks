'''
this algorithm only works for square matrix
'''

def rotateMatrix(matrix):
    top = left = 0
    bottom = len(matrix)-1
    right = len(matrix[0])-1
    
    while left < right and top < bottom:
         
        prev = matrix[top+1][left]
        
        for i in range(left,right+1):
            curr = matrix[top][i]
            matrix[top][i] = prev
            prev = curr

        top += 1


        for i in range(top,bottom+1):
            curr = matrix[i][right]
            matrix[i][right] = prev
            prev = curr

        right -= 1


        for i in range(right,left-1,-1):
            curr = matrix[bottom][i]
            matrix[bottom][i] = prev
            prev = curr

        bottom -= 1


        for i in range(bottom,top-1,-1):
            curr = matrix[i][left]
            matrix[i][left] = prev
            prev = curr

        left += 1
    return matrix


def printMatrix(matrix):
    for row in matrix:
        print(row)

matrix = [  
            [1,  2,  3,  4 ], 
            [5,  6,  7,  8 ], 
            [9,  10, 11, 12 ], 
            [13, 14, 15, 16 ]   
        ]

matrix = rotateMatrix(matrix)

printMatrix(matrix)
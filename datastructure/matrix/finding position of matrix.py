'''
this is the optimised algroithm for finding 
position in matrix of an element
'''



def findMartix(matrix, x):
    i = 0
    j = len(matrix)-1
    while(i < len(matrix) and j>=0):
        if matrix[i][j]==x:
            print("number found  ",i,' ',j)
            return 
        else:
            if matrix[i][j]>x:
                j -= 1
            else:
                i += 1
    print("not found")
    

def printMatrix(matrix):
    for row in matrix:
        print(row)
x = 8
matrix = [ [1, 2, 3, 4 ], 
        [5, 6, 7, 8 ], 
        [9, 10, 11, 12 ], 
        [13, 14, 15, 16 ] ]


findMartix(matrix, x)


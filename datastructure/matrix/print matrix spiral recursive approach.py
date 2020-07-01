'''

Time  complexity of this algorithm is rows * columns
m*n time required to traverse the matrix

space complexity if your want to store value in the variable 
then you have to use a list of size m*n

it will take no extra space

time complexity is O(m*n)
space complexity is O(1)


two approach for solving this prooblem

#@ Normal approach

#@ recursive approach



'''

"""

This method is the recursive approach of solving this problem

"""

def printSpiral(matrix,top,bottom,right,left):

    if top>=bottom or left >= right:
        return 

    for i in range(left,right+1):
        print(matrix[top][i],end=" ")
    top += 1    

    for i in range(top,bottom+1):
        print(matrix[i][right],end=" ")
    right -= 1

    for i in range(right,left-1,-1):
        print(matrix[bottom][i],end=" ")
    bottom -= 1

    for i in range(bottom,top-1,-1):
        print(matrix[i][left],end=" ") 
    left += 1
    printSpiral(matrix,top,bottom,right,left)

def printMatrix(matrix):
    for rows in matrix:
        print(rows)


matrix = [
    [1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]
]
printMatrix(matrix)
print("----------------------------------------")
printSpiral(matrix,0,3,4,0)

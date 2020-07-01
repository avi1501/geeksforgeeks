'''

Time  complexity of this algorithm is rows * columns
m*n time required to traverse the matrix

space complexity if your want to store value in the variable 
then you have to use a list of size m*n

but if you simply want to print the value then 
it will take no extra space
 we are doing two approach here first 

#@ Normal approach

#@ recursive approach



'''

"""

This method is the simple way of solving this problem

"""

def giveSpiral(matrix):
    top = left = 0
    right = len(matrix[0])-1
    bottom = len(matrix)-1

    listi = []

    while(top<bottom and left<right):
        for i in range(left,right+1):
            listi.append(matrix[top][i])
        top += 1

        for i in range(top,bottom+1):
            listi.append(matrix[i][right])
        right -= 1

        for i in range(right,left-1,-1):
            listi.append(matrix[bottom][i])
        bottom -= 1

        for i in range(bottom,top-1,-1):
            listi.append(matrix[i][left])
        left += 1
    return listi

def printMatrix(matrix):
    for rows in matrix:
        print(rows)


matrix = [
    [1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]
]
printMatrix(matrix)
print("hold your breath ")
listi = giveSpiral(matrix)
print(listi)
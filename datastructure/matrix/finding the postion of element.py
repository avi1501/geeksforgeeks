def findPos(matrix,fromrow,torow,fromcol,tocol,key):
    i = fromrow + (torow-fromrow)//2
    j = fromcol + (tocol-fromcol)//2
    if matrix[i][j]== key:
        print("key found")
    else:

        if i != torow or j != fromcol:
            findPos(matrix,fromrow,i,j,fromcol,key)

        if  fromrow == torow and fromcol+1 == tocol:
            if matrix[torow][tocol] == key:
                print("key found")

        if matrix[i][j]<key:
            if i+1 <=torow:
                findPos(matrix,i+1,torow,fromcol,tocol,key)
        else:
            if j-1>= fromcol:
                findPos(matrix,fromrow,torow,fromcol,j-1,key)
mat = [[ 10, 20, 30, 40], 
           [15, 25, 35, 45], 
           [27, 29, 37, 48], 
           [32, 33, 39, 50]]; 
n = 0
rowcount = 4; colCount = 4; key = 50; 
for i in range(rowcount): 
    for j in range(colCount): 
        findPos(mat, 0, rowcount - 1, 0, colCount - 1, mat[i][j]);
        n += 1
print(n) 
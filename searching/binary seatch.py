'''
binary search is a method of searching
In this we use divide and conquer method for the operation
time complexity for this technique is
best case -O(1)
avg and worst case -O(logn)

better than linear search

'''



a=[1,5,3,6,4,9,8]
a.sort()
# iteration method of binary search
#using loop
n=len(a)
x=9
lb=0
ub=n-1
posi="not found"
while(1):
    if(ub>=lb):
        mid=(lb+ub)//2
        if(a[mid]==x):
            posi=mid
            break
        elif(a[mid]>x):
            ub=mid-1
        else:
            lb=mid+1
    else:
        break
print(posi)
    
#recursive method of binary search
#using recursion 
def binarysearch(a,x,lb,ub):
    if(lb<=ub):
        mid=(lb+ub)//2
        if(a[mid]==x):
            return mid
        elif(a[mid]>x):
            return binarysearch(a,x,lb,mid-1)
        else:
            return binarysearch(a,x,mid+1,ub)
    return 'not found'
def binary_search(a,x):
    n=len(a)
    lb=0
    ub=n-1
    return binarysearch(a,x,lb,ub)
print(binary_search(a,x))
    
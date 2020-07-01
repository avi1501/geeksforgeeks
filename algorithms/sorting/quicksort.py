a=[20,30,40,29,11,55,41,47,99,45,60]

'''

first way to implement quicksort in easy way
but second way is not using any extra memory

'''
def quicksort(arr):     
    if(len(arr)<=1):
        return arr
    pivot=arr[0]
    big=[]
    small=[]
    piv=[]
    for i in arr:
        if(pivot>i):
            small.append(i)
        elif(pivot<i):
            big.append(i)
        else:
            piv.append(i)
    return quicksort(small)+piv+quicksort(big)

'''
implemetation without using extra element
'''

def quick_sort(A,low,hi):
    if(low<hi):
        p=partition(A,low,hi)
        quick_sort(A,low,p)
        quick_sort(A,p+1,hi)
def partition(A,low,hi):
    pivot=low
    border=low
    for i in range(low,hi):
        if A[i]<A[pivot]:
            border+=1
            A[border],A[i]=A[i],A[border]
    A[border],A[pivot]=A[pivot],A[border]
    return border
        
so=len(a)
quick_sort(a,0,so)
print(a)








def partition(hi,low,arr):
    pivot = low
    border = low
    
a=[20,30,40,29,11,55,41,47,99,45,60]
def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        key=arr[i]
        while(j>=0 and a[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
insertionsort(a)
print(a)

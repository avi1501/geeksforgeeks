a=[20,30,40,29,11,55,41,47,99,45,60]
def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        mi=arr.index(min(arr[i:]))
        arr[i],arr[mi]=arr[mi],arr[i]

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        mi=i
        for j in range(i+1,n):
            if(arr[mi]>arr[j]):
                mi=j
        arr[i],arr[mi]=arr[mi],arr[i]
selection_sort(a)
print(a)
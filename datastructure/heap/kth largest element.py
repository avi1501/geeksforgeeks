'''
Method 1
use bubble k times


'''
'''
This program have the time complexity of O(nk)
'''
arr = [1,23,12,9,30,2,50]
k = 3
n = 0
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
    if n != k:
        n += 1
        print(arr[j+1]) 

print("1st method over new method below")
'''
best method is to use the tim sort
which is default in python
use the sort method

'''

arr = [1,23,12,9,30,2,50]
arr.sort()
k=3
for i in range(k):
    print(arr[len(arr)-i-1])


print("using the max heap for finding the max element")
''' 
using the max heap 

Build the max heap in O(n)
the extract max k times to fet k maximum element from the maxheap in O(klogn)

so total time complexity for this is O(n+klogn)
'''
print("heap one is started")

def heapify(arr,n,i):
    largest = i
    l = i*2+1
    r = i*2+2
    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr,n,largest)
    

def heapsort(arr,k):
    n = len(arr)
    print(n)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    print(arr)
    counter = 0
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)
        if k <= 0:
            return
        k -= 1
        counter += 1
        print(arr[-counter])


arr = [1,23,12,9,30,2,50]

heapsort(arr,k)

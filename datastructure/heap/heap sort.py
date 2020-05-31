def heapify(arr,n,i):
    largest = i
    l = i*2+1
    r = i*2+2
    if l < n and arr[l] > arr[i]:
        print('left')
        largest = l
    if r < n and arr[r] > arr[largest]:
        print('right')
        largest = r
    if largest != i:
        print('swap')
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr,n,largest)
    

def heapsort(arr):
    n = len(arr)
    print(n)
    for i in range(n//2-1,-1,-1):
        print("in heap")
        heapify(arr,n,i)
    print('afd')
    print(arr)
    print('afd')
    
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)


arr  = [12, 11, 13, 5, 6, 7]

heapsort(arr)
print("Sorted array is")
print(arr)


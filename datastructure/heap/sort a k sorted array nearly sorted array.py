"""
for sorting array of of k sorted array 
we can use normal sort algorithm 
for this we can use merge sort for 
getting time complexity of O(nlogn)



"""
'''
But we can reduce the time complexity 
of this thing by using the min heap for
sorting this array

using prebuilt heap for this thing
'''


from heapq import heappush, heappop, heapify
arr = [6, 5, 3, 2, 8, 10, 9]
heap=[]
sortarray = []
k=3

for i in range(len(arr)):
    heappush(heap,arr[i])
    if len(heap)>k:
        sortarray.append(heappop(heap))
while(heap):
    sortarray.append(heappop(heap))

print(sortarray)

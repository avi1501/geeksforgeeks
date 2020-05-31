from heapq import heapify,heappush,heappop

heap = []
heapify(heap)

heappush(heap,10)
heappush(heap,20)
heappush(heap,30)
heappush(heap,40)

print("head value of the heap is ",heap[0])

print("elements of the heap is :")
for i in heap:
    print(i,end=" ")
print()

element = heappop(heap)
print("element popped from heap is ",element)

for i in heap:
    print(i,end=" ")
print()

element = heappop(heap)
print("element popped from heap is ",element)

for i in heap:
    print(i,end=" ")
print()

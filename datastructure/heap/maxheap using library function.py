''' we are multiplying the value with -1
beacaus the library function supports min 
heap by default'''



from heapq import heappop,heappush,heapify

heap = []
heapify(heap)
heappush(heap,-1*10)
heappush(heap,-1*20)
heappush(heap,-1*30)
heappush(heap,-1*40)

print("head value of the heap :"+str(-1*heap[0]))
print("the heap elements are :")
for i in heap:
    print(-1*i,end = " ")
print()

element = heappop(heap)
print("element popped",-1*element)

for i in heap:
    print(-1*i,end=" ")
print()

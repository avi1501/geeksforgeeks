import sys
class MaxHeap:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0]*maxsize
        self.heap[0] = sys.maxsize
        self.front = 1
    
    def parent(self,pos):
        return pos//2

    def leftChild(self,pos):
        return 2*pos
    
    def rightChild(self,pos):
        return 2*pos+1
    
    def isLeaf(self,pos):
        if pos>=self.size//2 and pos <=self.size:
            return True
        return False
    
    def swap(self,fpos,lpos):
        self.heap[fpos],self.heap[lpos] = self.heap[lpos],self.heap[fpos]

    def insert(self,element):
        if self.size >= self.maxsize:
            return 
        
        self.size += 1
        current = self.size
        self.heap[current] = element
        while(self.heap[current] > self.heap[self.parent(current)]):
            self.swap(current,self.parent(current))
            current = self.parent(current)
    
    def Print(self):
        for i in range(1,len(self.heap)):
            if self.heap[i] != 0:
                print(self.heap[i], end =" ")
        print()
        
    
    def pop(self):
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.heap[self.size] = 0
        self.size -= 1
        self.heapify(self.front)
        return popped
    def heapify(self,pos):
        if not self.isLeaf(pos):
            if self.heap[pos] < self.heap[self.leftChild(pos)] or self.heap[pos] < self.heap[self.rightChild(pos)]:
                if self.heap[self.leftChild(pos)] > self.heap[self.rightChild(pos)]:
                    self.swap(pos,self.leftChild(pos))
                    self.heapify(self.leftChild(pos))
                else:
                    self.swap(pos,self.rightChild(pos))
                    self.heapify(self.rightChild(pos))


        
if __name__ == "__main__": 
    print('The maxHeap is ') 
    minHeap = MaxHeap(15) 
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    # minHeap.insert(19) 
    # minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
  
    minHeap.Print() 
    print(minHeap.pop())
    # print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
   
    
    minHeap.Print()

    
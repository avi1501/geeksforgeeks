import sys
class minheap:
    def __init__(self,capacity):
        self.maxsize = capacity
        self.currsize = 0
        self.heap = [0]*capacity
        self.heap[0] = float('-inf')
        self.front = 1
    
    def parent(self,pos):
        return pos//2
    
    def leftChild(self,pos):
        return pos*2
    
    def rightChild(self,pos):
        return pos*2+1
    
    def isLeaf(self,pos):
        if pos <= self.maxsize and pos>= self.currsize//2:
            return True
        return False  
    
    def swap(self,fpos,lpos):
        self.heap[fpos],self.heap[lpos] = self.heap[lpos],self.heap[fpos]
    
    def insert(self,value):
        if self.currsize >= self.maxsize:
            return
        self.currsize += 1
        pos = self.currsize
        self.heap[self.currsize] = value
        while self.heap[self.parent(pos)] > self.heap[pos]:
            self.swap(pos,self.parent(pos))
            pos = self.parent(pos)
    def Print(self):
        for i in range(1,self.currsize+1):
            if self.heap[i] !=  0:
                print(self.heap[i],end = " ")
        print()
    
    def pop(self):
        if self.currsize>0:
            popped = self.heap[self.front]
            self.heap[self.front] = self.heap[self.currsize]
            self.heap[self.currsize] = 0
            self.heapify(self.front)
            return popped
        else:
            return "no element in the heap"
        
    def heapify(self,pos):
        if not self.isLeaf(pos):
            if self.heap[pos] > self.heap[self.leftChild(pos)] or self.heap[pos] > self.heap[self.rightChild(pos)]:
                if self.heap[self.leftChild(pos)] > self.heap[self.rightChild(pos)]:
                    self.swap(pos,self.rightChild(pos))
                    self.heapify(self.rightChild(pos))
                else:
                    self.swap(pos,self.leftChild(pos))
                    self.heapify(self.leftChild(pos)) 
    



if __name__ == "__main__": 
    print('The maxHeap is ') 
    minHeap = minheap(15) 
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
  
    minHeap.Print() 
    print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
    print("popping the minimum element ",minHeap.pop())
    
    minHeap.Print()




        
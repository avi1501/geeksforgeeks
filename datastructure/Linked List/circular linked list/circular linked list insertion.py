class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self,data):
        if self.last == None:
            temp = Node(data)
            self.last = temp
            self.last.next = self.last
            return True
        else:
            return False


    def addBegin(self,data):
        if self.addToEmpty(data):
            print('empty function')
            return 
        node = Node(data)
        node.next = self.last.next
        self.last.next = node

    def addEnd(self,data):
        if self.addToEmpty(data):
            return 
        node = Node(data)
        node.next = self.last.next
        self.last.next = node
        self.last = node
    
    def addAfter(self,data,after):
        if self.addToEmpty(data):
            return 
        if after == self.last.data:
            addEnd(data)
            return
        temp = self.last.next
        while(temp.data != after):
            temp = temp.next
        node = Node(data)
        node.next = temp.next
        temp.next = node
    
    def traverse(self):
        if self.last == None:
            print("list is empty")
            return 
        temp = self.last.next
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
            if temp == self.last.next:
                break

llist = CircularLinkedList() 
  
llist.addToEmpty(6) 
llist.addBegin(4)
last = llist.addBegin(2) 
last = llist.addEnd(8) 
last = llist.addEnd(12) 
last = llist.addAfter(10,8)


llist.traverse() 




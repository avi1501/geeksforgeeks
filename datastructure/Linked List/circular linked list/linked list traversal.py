class Node:  
    def __init__(self, data): 
        self.data = data  
        self.next = None
  
class CircularLinkedList: 
    def __init__(self): 
        self.head = None
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
            return 
        ptr1 = Node(data)
        ptr1.next = self.head
        temp = self.head
        while(temp.next != self.head):
            temp = temp.next
        temp.next = ptr1
        self.head = ptr1
  
    def printList(self):
        temp = self.head
        flag = 0
        if self.head is not None:
            while True:
                print(temp.data,end=" ")
                temp = temp.next
                if temp == self.head:
                    break



cllist = CircularLinkedList() 
  
# Created linked list will be 11->2->56->12 
cllist.push(12) 
cllist.push(56) 
cllist.push(2) 
cllist.push(11) 
  
print("Contents of circular Linked List")
cllist.printList() 

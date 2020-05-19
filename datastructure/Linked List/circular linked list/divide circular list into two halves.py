class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
  
class CircularLinkedList: 
      
    def __init__(self): 
        self.head = None

    def push(self, data): 
        ptr1 = Node(data) 
        temp = self.head 
          
        ptr1.next = self.head 

        if self.head is not None: 
            while(temp.next != self.head): 
                temp = temp.next 
            temp.next = ptr1 
  
        else: 
            ptr1.next = ptr1
  
        self.head = ptr1  
  
    def printList(self): 
        temp = self.head 
        if self.head is not None: 
            while(True): 
                print(temp.data)
                temp = temp.next
                if (temp == self.head): 
                    break 
  
  
    def splitList(self, head1, head2): 
        n = 0
        temp = self.head
        while(temp):
            n += 1
            temp = temp.next
            if temp == self.head:
                break
        temp = self.head
        temp1 = head1.head =Node(0)
        temp2 = head2.head = Node(0)
        for i in range(n//2):
            temp1.next = Node(temp.data)
            temp1 = temp1.next
            temp = temp.next
        head1.head = head1.head.next
        temp1.next = head1.head
        for i in range(n-n//2):
            temp2.next = Node(temp.data)
            temp2 = temp2.next
            temp = temp.next
        head2.head = head2.head.next
        temp2.next = head2.head
            
                
        
            
        
  

head = CircularLinkedList()  
head1 = CircularLinkedList() 
head2 = CircularLinkedList() 
  
head.push(12) 
head.push(56) 
head.push(2) 
head.push(11) 
head.push(23)
  
print("Original Circular Linked List")
head.printList() 

head.splitList(head1 , head2) 
  
print("First Circular Linked List")
head1.printList() 
  
print("Second Circular Linked List")
head2.printList() 
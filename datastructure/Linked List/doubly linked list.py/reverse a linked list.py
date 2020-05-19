class Node: 

    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
  
class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
   
    def reverse(self): 
        temp = self.head
        while temp:
            temp.prev,temp.next = temp.next,temp.prev
            tstart = temp 
            temp = temp.prev
        self.head = tstart

          
    def push(self, new_data): 
   
        new_node = Node(new_data) 
   
        new_node.next = self.head 
   
        if self.head is not None: 
            self.head.prev = new_node 
   
        self.head = new_node 
  
  
    def printList(self, node): 
        while(node is not None): 
            print(node.data) 
            node = node.next
  
dll = DoublyLinkedList() 
dll.push(2); 
dll.push(4); 
dll.push(8); 
dll.push(10); 
  
print("Original Linked List")
dll.printList(dll.head) 

dll.reverse() 
  
print("Reversed Linked List")
dll.printList(dll.head) 
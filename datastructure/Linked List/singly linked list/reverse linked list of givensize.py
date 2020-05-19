
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
            return 
        temp=self.head
        while temp.next :
            temp = temp.next
        temp.next = Node(data)


    def printlinkedlist(self):
        temp=self.head
    
        while(temp):
            
            print(temp.data)
            temp=temp.next
    
    def reverseatgivensize(self,n):
        prev = self.head
        for i in range(n):
            prev = prev.next
        curr=self.head
        next=self.head
        for i in range(n):
            next = curr.next
            curr.next = prev
            prev = curr
            curr =next
        self.head = prev


llist=Linkedlist()
first = Node(1)
llist.head = first
second=Node(2)
first.next = second
third = Node(3)
second.next = third
fourth=Node(4)
third.next=fourth
fifth = Node(5)
fourth.next=fifth
sixth = Node(6)
fifth.next=sixth
seventh = Node(7)
sixth.next=seventh
eight = Node(8)
seventh.next=eight

size=4
llist.reverseatgivensize(size)

llist.printlinkedlist()
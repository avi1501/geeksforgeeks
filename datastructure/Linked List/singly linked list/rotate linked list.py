
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
    
    def rotatelinkedlist(self,no):
        temp = self.head
        end = self.head
        prev = None
        for i in range(no):
            prev = temp
            temp = temp.next
        while(end.next):
            end = end.next
        prev.next = None
        end.next = self.head
        self.head = temp
            

        

        


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

llist.rotatelinkedlist(3)
llist.printlinkedlist()

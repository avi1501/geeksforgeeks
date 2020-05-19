
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


    def detectandremoveloop(self):
        slow = fast = self.head
        while(slow and fast and fast.next):
            slow = slow.next
            fast=fast.next.next
            if slow == fast :
                print('loop exists')
                self.__remove(slow)
                return 
        print('loop not exists')
    
    def __remove(self,loopnode):
        ptr1=ptr2=loopnode
        size=1
        while(ptr2.next != ptr1):
            size += 1
            ptr2 = ptr2.next
        ptr1=self.head
        ptr2 = self.head
        while(size>0):
            size -= 1
            ptr2 = ptr2.next
        
        while(ptr1 != ptr2):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        while(ptr2.next != ptr1):
            ptr2 = ptr2.next
        ptr2.next=None

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
eight.next=fifth

llist.detectandremoveloop()

llist.printlinkedlist()



        







        

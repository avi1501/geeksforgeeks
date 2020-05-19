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
    
    def detectloop(self):
        slow= self.head
        fast = self.head
        flag = 0 
        while (slow != fast or flag == 0) and slow and fast and fast.next:
            flag = 1
            slow=slow.next
            fast=fast.next.next
        if slow == fast:
            print('loop exist')
            return True
        else:
            print('loop does not exist')
            return False
    
    def countlinkedlistsize(self):
        tracker = []
        temp = self.head
        count = 0
        while temp and temp not in tracker:
            tracker.append(temp)
            count += 1
            temp = temp.next
        return count
        
    def removeloop(self):
        if self.detectloop == False:
            print('no loop exist in linked list')
            return 
        slow = self.head
        fast = self.head
        flag = 0
        while (flag == 0 or slow != fast) and slow and fast:
            flag = 1        
            slow = slow.next
            fast = fast.next.next
        temp1=Linkedlist()
        temp1.head=self.head
        linkedListSize = temp1.countlinkedlistsize()
        
        temp2 = Linkedlist()
        temp2.head = slow
        circularListSize = temp2.countlinkedlistsize()
        
        headofcircular=self.head
        for i in range(linkedListSize-circularListSize):
            print(headofcircular.data)
            headofcircular = headofcircular.next
        
        tailofcircular = headofcircular
        
        for i in range(1,circularListSize):
            tailofcircular = tailofcircular.next
        tailofcircular.next = None
    
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
                print('loop exist')
                self.rem(slow)
                return 
        print('loop not exist')
    
    def rem(self,loopnode):
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

print('gdffsxdsfds')

llist.printlinkedlist()



        







        

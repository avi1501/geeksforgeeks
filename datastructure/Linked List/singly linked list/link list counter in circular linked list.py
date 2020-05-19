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
    

    def countlinkedlistsize(self):
        tracker = []
        temp = self.head
        count = 0
        while temp and temp not in tracker:
            print(temp.data)
            tracker.append(temp)
            count += 1
            temp = temp.next
        return count

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
si = llist.countlinkedlistsize()
print(si)

print('second linked list')
llist2 = Linkedlist()
llist2.head=seventh
si = llist2.countlinkedlistsize()
print(si)
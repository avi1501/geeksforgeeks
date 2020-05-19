class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self, data):
        temp=self.head
        while (temp.next):
            temp=temp.next
        temp.next = Node(data)
        del(temp)
    def reverselinkedlist(self):
       print('inside reverse function')
       if self.head == None:
           return 
       if self.head.next == None:
           return
       prev=None
       curr=self.head
       next=curr.next
       while curr:
           next=curr.next
           curr.next=prev
           prev=curr
           curr=next
       self.head=prev


llist=linkedlist()
llist.head=Node(1)
second=Node(2)
third=Node(3)
llist.head.next=second
second.next=third

llist.insert(8)
llist.insert(9)
llist.insert(10)
print('linked list before reversing')
temp=llist.head
while temp:
    print(temp.data)
    temp = temp.next
print('linked list after reversing')
llist.reverselinkedlist()
temp=llist.head
while temp:
    print(temp.data)
    temp = temp.next
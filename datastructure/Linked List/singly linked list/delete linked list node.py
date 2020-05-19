class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=Node(data)
    def deleteatstart(self):
        self.head=self.head.next
    def deletenode(self,data):
        temp=self.head
        while(temp.next.data!=data):
            temp=temp.next
        temp.next=temp.next.next

    def deleteendnode(self):
        temp=self.head
        if temp.next==None:
            self.head=None
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None

llist=linkedlist()
llist.head=Node(1)
second=Node(2)
third=Node(3)
llist.head.next=second
second.next=third

llist.insert(8)
llist.insert(9)
llist.insert(10)

temp=llist.head
while(temp):
    print(temp.data)
    temp=temp.next

llist.deleteatstart()
print('after deleting from start')
temp=llist.head
while(temp):
    print(temp.data)
    temp=temp.next

llist.deletenode(9)
print('after deleting 9')
temp=llist.head
while(temp):
    print(temp.data)
    temp=temp.next
llist.deleteendnode()
print("after deleting last node")
temp=llist.head
while(temp):
    print(temp.data)
    temp=temp.next




        
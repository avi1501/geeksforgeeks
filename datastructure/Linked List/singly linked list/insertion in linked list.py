class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insertatstart(self,data):
        start=Node(data)
        start.next=self.head
        self.head=start
    def insertaftergivennode(self,data,targetnode):
        node=Node(data)
        temp=self.head
        while(temp):
            if(temp.data==targetnode):
                break
            temp=temp.next
        node.next=temp.next
        temp.next=node
    def insertatlast(self,data):
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=Node(data)
    
    
llist=linkedlist()
llist.head=Node(1)
second=Node(2)
third=Node(3)
llist.head.next=second
second.next=third

llist.insertatstart(8)
llist.insertaftergivennode(9,2)
llist.insertatlast(10)

temp=llist.head
while(temp):
    print(temp.data)
    temp=temp.next

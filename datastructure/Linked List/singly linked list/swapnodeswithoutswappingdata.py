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
    def swapnodes(self, x, y):
        temp = self.head
        prevx = None
        currx = self.head
        while(currx and currx.data != x):
            prevx=currx
            currx=currx.next
        prevy=None
        curry=self.head
        while(curry and curry.data != y):
            prevy=curry
            curry=curry.next
        if curry == None and currx == None :
            return
        if prevx !=None:
            prevx.next=curry
        else:
            self.head=curry
        if prevy != None :
            prevy.next=currx
        else :
            self.head = currx
        
        currx.next,curry.next=curry.next,currx.next


llist=linkedlist()
llist.head=Node(1)
second=Node(2)
third=Node(3)
llist.head.next=second
second.next=third

llist.insert(8)
llist.insert(9)
llist.insert(10)

temp = llist.head
while temp:
    print(temp.data)
    temp=temp.next

print('after swapping 2 and 8')
llist.swapnodes(2,8)
temp = llist.head
while temp :
    print(temp.data)
    temp=temp.next


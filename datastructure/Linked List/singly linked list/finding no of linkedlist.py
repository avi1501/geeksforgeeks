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
    def noofnodes(self):
        count=0
        temp=self.head
        while (temp):
            count = count+1
            temp = temp.next
        print(count)
        del(count)

    def helperfunction(self, temp):
        if (temp == None):
            return 0
        return 1 + self.helperfunction(temp.next)
    def noofnodesrecursive(self):
        print(self.helperfunction(self.head))

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

print('no of nodes are',end=" ")
llist.noofnodes()
print('no of nodes recursively',end=" ")
llist.noofnodesrecursive()
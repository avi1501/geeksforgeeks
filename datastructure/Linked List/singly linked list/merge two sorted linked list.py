class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self, data):
        if self.head == None:
            self.head=Node(data)
            return
        temp=self.head
        while (temp.next):
            temp=temp.next
        temp.next = Node(data)
        del(temp)
    def printlinkedlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def __add__(self,o):
        firsttemp = self.head
        secondtemp = o.head
        newlist=linkedlist()
        newlist.insert(0)
        temp=newlist.head
        while firsttemp and secondtemp:
            if firsttemp.data > secondtemp.data:
                temp.next = Node(secondtemp.data)
                secondtemp = secondtemp.next
            else:
                temp.next = Node(firsttemp.data)
                firsttemp=firsttemp.next
            
            temp=temp.next
        if firsttemp:
            temp.next=firsttemp
        else:
            temp.next = secondtemp
        newlist.head=newlist.head.next
        return newlist



llist1 = linkedlist()
llist1.insert(5)
llist1.insert(10)
llist1.insert(15)
llist2 = linkedlist()
llist2.insert(2)
llist2.insert(3)
llist2.insert(20)
print('linked list 1')
llist1.printlinkedlist()

print('linked list 2')
llist2.printlinkedlist()
print('After the addition of linked list')
llist3 = llist1 + llist2
llist3.printlinkedlist()





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
            
            print(temp.data,end=" ")
            temp=temp.next
        print()
    
    def addtwolist(self,list1,list2):
        l1=list1.head
        l2=list2.head
        l3=None
        if l1 == None:
            return list2
        elif(l2 == None):
            return list1
        while l1 and l2 :
            carry = 0
            sumdata=l1.data+l2.data
            if sumdata>9:
                carry = sumdata // 10
                sumdata = sumdata % 10
            l3 = Node(sumdata+carry)
            
    
    

llist1=Linkedlist()
first = Node(5)
llist1.head = first
second=Node(6)
first.next = second
third = Node(3)
second.next = third

llist2=Linkedlist()
first = Node(8)
llist2.head = first
second=Node(4)
first.next = second
third = Node(2)
second.next = third

print('linked list 1')
llist1.printlinkedlist()
print('linked list 2')
llist2.printlinkedlist()

llist3 = Linkedlist()
llist3.addtwolist(llist1,llist2)





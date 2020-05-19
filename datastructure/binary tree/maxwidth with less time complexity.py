class Node: 
      
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def getMaxWidth(root): 
    if root == None:
        return 0
    queue = []
    maxwidth = 0
    queue.insert(0,root)
    while(queue is not None):
        count =len(queue)
        maxwidth=max(maxwidth,count)
        while(count>0):
            count -= 1
            temp =queue[-1]
            queue.pop()
            if temp.left is not None:
                queue.insert(0,temp.left)
            if temp.right is not None:
                queue.insert(0,temp.right)
    return maxwidth



  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.right = Node(8) 
root.right.right.left = Node(6) 
root.right.right.right = Node(7)  
  
""" 
Constructed bunary tree is: 
    1 
    / \ 
    2 3 
    / \     \ 
4 5 8  
        / \ 
        6 7 
"""
  
print("Maximum width is %d" %(getMaxWidth(root))) 
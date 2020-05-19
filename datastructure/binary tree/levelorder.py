class Node: 
  
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None
  
  
def height(root):
    if root == None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)

    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1

def printlevelorder(root):
    h = height(root)
    for i in range(1,h+1):
        givenlevel(root,3)

def givenlevel(root,h):
    if root == None:
        return
    if h == 1:
        print("%d"%root.data,end=" ")
    elif h > 1:
        givenlevel(root.left,h-1)
        givenlevel(root.right,h-1)

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
print("Level order traversal of binary tree is -")
printlevelorder(root) 
print()
'''
above solution takes time complexity of O(n^2)
this take O(n) space complexity in wrost case
this one is not efficient one for printing the 
level order

'''

'''
we can print the level order traversal using 
queue 
with the queue we can traverse this in the complexity 
of O(n)
for worst case for both time and space complexity


'''
def printlevelorderusingqueue(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    while(queue):
        node = queue.pop(0)
        print(node.data,end =" ")
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
del(root)

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
print("Level Order Traversal of binary tree is -",end=" ")
printlevelorderusingqueue(root) 

printlevelorder
        


    

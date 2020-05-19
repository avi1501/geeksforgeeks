class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None
  

def inorderSuccessor(root,key):
    if root.data == key.data:
        temp = root.right
        while(temp.left):
            temp = temp.left
        return temp
    elif root.data > key.data:
        return inorderSuccessor(root.left,key)
    elif root.data < key.data:
        return inorderSuccessor(root.right,key)
    else:
        return None

def insert( node, data): 
  
    # 1) If tree is empty then return a new singly node 
    if node is None: 
        return Node(data) 
    else: 
         
        # 2) Otherwise, recur down the tree 
        if data <= node.data: 
            temp = insert(node.left, data) 
            node.left = temp  
            temp.parent = node 
        else: 
            temp = insert(node.right, data) 
            node.right = temp  
            temp.parent = node 
          
        # return  the unchanged node pointer 
        return node 
  
  
# Driver progam to test above function 
  
root  = None
  
# Creating the tree given in the above diagram  
root = insert(root, 20) 
root = insert(root, 8); 
root = insert(root, 22); 
root = insert(root, 4); 
root = insert(root, 12); 
root = insert(root, 10);   
root = insert(root, 14);     
temp = root.left.right.right  
  
succ = inorderSuccessor( root, temp) 
if succ is not None: 
    print ("Inorder Successor of %d is %d " %(temp.data , succ.data)) 
else: 
    print ("\nInorder Successor doesn't exist")
  

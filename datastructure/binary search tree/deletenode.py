class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
  
  
# A utility function to do inorder traversal of BST 
def inorder(root): 
    if root is not None: 
        inorder(root.left) 
        print(root.key) 
        inorder(root.right) 
  
  
# A utility function to insert a new node with given key in BST 
def insert( node, key): 
  
    # If the tree is empty, return a new node 
    if node is None: 
        return Node(key) 
  
    # Otherwise recur down the tree 
    if key < node.key: 
        node.left = insert(node.left, key) 
    else: 
        node.right = insert(node.right, key) 
  
    # return the (unchanged) node pointer 
    return node 
  
# Given a non-empty binary search tree, return the node 
# with minum key value found in that tree. Note that the 
# entire tree does not need to be searched  
def minValueNode( node): 
    current = node
    if current.left is not None:
        current = current.left
    
    return current
  
# Given a binary search tree and a key, this function 
# delete the key and returns the new root 
def deleteNode(root, key): 
    if root == None:
        return root
    elif(root.key>key):
        root.left = deleteNode(root.left,key)
    elif(root.key<key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        minvalue = minValueNode(root)
        root.key = minvalue.key
        root.right = deleteNode(root.right,minvalue.key)

    return root
  
    
# Driver program to test above functions 
""" Let us create following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80 """
  
root = None
root = insert(root, 50) 
root = insert(root, 30) 
root = insert(root, 20) 
root = insert(root, 40) 
root = insert(root, 70) 
root = insert(root, 60) 
root = insert(root, 80) 
  
print ("Inorder traversal of the given tree")
inorder(root) 
  
print ("\nDelete 20")
root = deleteNode(root, 20) 
print ("Inorder traversal of the modified tree")
inorder(root) 
  
print ("\nDelete 30")
root = deleteNode(root, 30) 
print ("Inorder traversal of the modified tree")
inorder(root) 
  
print ("\nDelete 50")
root = deleteNode(root, 50) 
print ("Inorder traversal of the modified tree")
inorder(root) 
class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data  = data  
        self.left = None
        self.right = None

def getarrayfrombst(root,arr):
    if root == None:
        return 
    getarrayfrombst(root.left,arr)
    arr.append(root.data)
    getarrayfrombst(root.right,arr)  
def inorderbst(arr,root):
    if root == None:
        return
    inorderbst(arr,root.left)
    root.data = arr.pop(0)
    inorderbst(arr,root.right)

def inordertraversal(root):
    if root == None:
        return 
    inordertraversal(root.left)
    print(root.data,end=" ")
    inordertraversal(root.right)

def binaryTreeToBST(root):
    if root == None:
        return root
    arr = []
    getarrayfrombst(root,arr) 
    arr.sort()
    inorderbst(arr,root)
    


  
# Driver program to test above function 
root = Node(10) 
root.left = Node(30) 
root.right = Node(15) 
root.left.left = Node(20) 
root.right.right= Node(5) 
  
# Convert binary tree to BST  
binaryTreeToBST(root) 
  
print("Following is the inorder traversal of the converted BST")
inordertraversal(root) 
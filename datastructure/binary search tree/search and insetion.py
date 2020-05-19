class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,node):
    if root == None:
        root = node
    else:
        if root.data > node.data:
            if root.left:
                insert(root.left,node)
            else:
                root.left = node
        else:
            if root.right:
                insert(root.right,node)
            else:
                root.right = node

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

inorder(r) 

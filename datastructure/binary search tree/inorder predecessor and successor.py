'''
in a given tree 

'''


class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.key  = key 
        self.left = None
        self.right = None
#In order predecessor 
#   write your code here
def pred(root,key):
    pre = 0
    succ = 0
    temp = root.left
    while(temp.right):
        temp = temp.right
    print(temp.right.key)
     





# def succ(root,key):
#     data = root.key
#     temp = root.right
#     while(temp.left):
#         if key>temp.key:
#             data = temp.key
#         temp = temp.left
#     return data


# if p=50
'''if p.left is not null:
        temp = root.left
        pred = p.left.data
        while(temp.right):
            temp = temp.right


    pred = root.data
    while(temp.data != key and temp != None)
        pred = temp.data
        temp = temp.left 
    if temp ==None:
        return data not found
    
    
    
    
    if root == key
    pred = root.data
    temp = root.left


'''
        
            
        

  
# A utility function to insert a new node in with given key in BST 
def insert(node , key): 
    if node is None: 
        return Node(key) 
  
    if key < node.key: 
        node.left = insert(node.left, key) 
  
    else: 
        node.right = insert(node.right, key) 
  
    return node 
  
  
# Driver program to test above function 
key = 65 #Key to be searched in BST 
   
""" Let us create following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80  
"""
root = None
root = insert(root, 50) 
insert(root, 30); 
insert(root, 20); 
insert(root, 40); 
insert(root, 70); 
insert(root, 60); 
insert(root, 80); 
  
# Static variables of the function findPreSuc  
print(pred(root,40))
  

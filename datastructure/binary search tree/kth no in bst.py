class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None

def helperfunction(root,count,k):
    helperfunction.count = count
    if root == None:
        return None
    left = helperfunction(root.left,helperfunction.count,k)
    if left != None:
        return left
    helperfunction.count += 1
    if helperfunction.count == k:
        return root
    return helperfunction(root.right,helperfunction.count,k)
  
def printKthelement(root,k):
    ret = helperfunction(root,0,k)
    if ret == None:
        return "there is less no of nodes"
    else:
        return "the k th no of node is ",ret.data



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
printKthelement.count = 0
print(printKthelement(root,4))
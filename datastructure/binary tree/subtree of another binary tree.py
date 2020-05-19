class Node: 

    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def isidentical(t1,t2):
    if t1 == None and t2 == None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.data == t2.data:
        return isidentical(t1.left,t2.left) and isidentical(t1.right,t2.right)
        
  
def isSubtree(T,S):
    if S is None:
        return True
    if T is None:
        return False
    if isidentical(T,S):
        return True
    return isSubtree(T.left,S) or isSubtree(T.right,S)


T = Node(26) 
T.right = Node(3) 
T.right.right  = Node(3) 
T.left = Node(10) 
T.left.left = Node(4) 
T.left.left.right = Node(30) 
T.left.right = Node(6) 
  

S = Node(10) 
S.right = Node(6) 
S.left = Node(4) 
S.left.right = Node(30) 
  
if isSubtree(T, S): 
    print("Tree 2 is subtree of Tree 1")
else : 
    print("Tree 2 is not a subtree of Tree 1")
class newNode: 
    def __init__(self, data: int): 
        self.data = data 
        self.left = None
        self.right = None
  
def inorder(root: newNode): 
  
    if root: 
        inorder(root.left) 
        print(root.data, end=" ") 
        inorder(root.right) 
  
def merge(root1: newNode, root2: newNode): 
  
    s1=[]
    s2 = []
    current1 = root1
    current2 = root2
    if current1 == None:
        return inorder(root2)
    if current2 == None:
        return inorder(root1)
    
    while(current1 or s1 or current2 or s2):
        if current1 or current2:
            if current1:
                s1.append(current1)
                current1 = current1.left
            if current2:
                s2.append(current2)
                current2 = current2.left
        else:
            if not s1:
                while(s2):
                    current2 = s2.pop()
                    current2.left = None
                    inorder(current2)
                    return

            if not s2:
                while(s1):
                    current1 = s1.pop()
                    current1.left = None
                    inorder(current1)
                    return

            current1 = s1.pop()
            current2 = s2.pop()


            if current1.data>current2.data:
                print(current2.data,end=" ")
                current2 = current2.right
                s1.append(current1)
                current1 = None
            else:
                print(current1.data,end=" ")
                current1 = current1.right
                s2.append(current2)
                current2 = None
 
  
def main(): 
  
    # Let us create the following tree as first tree 
    #      3 
    #     / \ 
    #    1   5 
  
    root1 = newNode(3) 
    root1.left = newNode(1) 
    root1.right = newNode(5) 
  
    # Let us create the following tree as second tree 
    #      4 
    #     / \ 
    #    2   6 
    # 
  
    root2 = newNode(4) 
    root2.left = newNode(2) 
    root2.right = newNode(6) 
    root2.right.right = newNode(10)
  
    merge(root1, root2) 
  
  
if __name__ == "__main__": 
    main() 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        self.nextRight = None
  
    def __str__(self): 
        return '{}'.format(self.data) 

def printnextright(root):
    if root:
        if root.nextRight:
            print(root.nextRight.data)
        else:
            printnextright(root.left)
            printnextright(root.right)

def connect(root):
    queue=[]
    queue.append(root)
    queue.append(None)
    while(queue):
        p = queue.pop(0)
        if p:
            p.nextright = queue[0]
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        elif queue:
            queue.append(None)

  

  
def main(): 
    """Driver program to test above functions. 
        Constructed binary tree is 
                10 
               /  \ 
             8      2 
            /        \ 
          3            90 
    """
  
    root = Node(10) 
    root.left = Node(8) 
    root.right = Node(2) 
    root.left.left = Node(3) 
    root.right.right = Node(90) 
    
  
    # Populates nextRight pointer in all nodes 
    connect(root) 
    print(root.left.nextright.data)
if __name__=="__main__":
    main()

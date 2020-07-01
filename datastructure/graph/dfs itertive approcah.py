class graph:
    def __init__(self,size):
        self.V=size
        self.adj=[[] for _ in range(self.V)]
    
    def addEdge(self,v,w):
        self.adj[v].append(w)
        
    def dfs(self,root):
        visited=[False for _ in range(self.V)]
        stack=[]
        stack.append(root)
        while(len(stack)):
            root=stack.pop()

            if not visited[root]:
                print(root,end=" ")
                visited[root]=True
            for i in self.adj[root]:
                if not visited[i]:
                    stack.append(i)
        print()

g = graph(5); # Total 5 vertices in graph  
g.addEdge(1, 0);  
g.addEdge(0, 2);  
g.addEdge(2, 1);  
g.addEdge(0, 3);  
g.addEdge(1, 4);  
  
print("Following is Depth First Traversal")  
g.dfs(0) 
from collections import defaultdict
class graph:
    def __init__(self,v):
        self.V=v
        self.graph=defaultdict(list)
        self.r=[[0 for i in range(self.V)] for j in range(self.V)]
    
    def addEdge(self,a,b):
        self.graph[a].append(b)
        self.graph[b]=self.graph[b]
    
    def __dfs(self,x,y):
        self.r[x][y]=1
        for i in self.graph[y]:
            if self.r[x][i]==0:
                self.__dfs(x,i)
    
    def transitiveClosure(self):
        for i in range(self.V):
            self.__dfs(i,i)
        print(self.r)

g = graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  

g.transitiveClosure(); 
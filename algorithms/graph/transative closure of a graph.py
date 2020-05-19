from collections import defaultdict
class graph:
    def __init__(self,v):
        self.V=v
        self.graph=defaultdict(list)
        self.rm=[[0 for j in range(v)] for i in range(v)]

    def addEdge(self,a,b):
        self.graph[a].append(b)
        self.graph[b]=self.graph[b]
    
    def __dfs(self,p,q):
        self.rm[p][q]=1
        for i in self.graph[q]:
            if self.rm[p][i]==0:
                self.__dfs(p,i)

    def transitiveClosure(self):
        for i in range(self.V):
            self.__dfs(i,i)
        print(self.rm)

g = graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  

g.transitiveClosure(); 
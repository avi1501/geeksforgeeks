from collections import defaultdict

class graph:
    def __init__(self,le):
        self.V=le
        self.graph=defaultdict(list)

    def addEdge(self,x,y):
        self.graph[x].append(y)
        self.graph[y]=self.garaph[y]
    
    def helperfunction(self,v,visited,recStack):
        visited[v]=True
        recStack[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                if self.helperfunction(i,visited,recStack) == True:
                    return True
            elif recStack[i]==True:
                    return True
        recStack[v]=False
        return False
    def isCyclic(self): 
        visited = [False] * self.V 
        recStack = [False] * self.V 
        for node in range(self.V): 
            if visited[node] == False: 
                if self.helperfunction(node,visited,recStack) == True: 
                    return True
        return False
    
g = graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
if g.isCyclic() == 1: 
    print("Graph has a cycle")
else: 
    print("Graph has no cycle")


        
            

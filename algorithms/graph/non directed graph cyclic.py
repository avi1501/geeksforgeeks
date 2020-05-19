from collections import defaultdict
class graph:
    def __init__(self,v):
        self.V=v
        self.graph=defaultdict(list)
    
    def addEdge(self,a,b):
        self.graph[a].append(a)
        self.graph[b].append(a)

    def __helperfunction(self,root,visited,parent):
        visited[root] = True
        for i in self.graph[root]:
            if visited[i] == False:
                if self.__helperfunction(i,visited,root) == True:
                    return True
                elif parent != i:
                    return True
        return False

    
    def isCyclic(self):
        visited=[False]*self.V
        for i in range(self.V):
            if visited[i] == False:
                if self.__helperfunction(i,visited,-1) == True:
                    return True
        return False

g = graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 0) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
  
if g.isCyclic(): 
    print("Graph contains cycle")
else : 
    print("Graph does not contain cycle ")
g1 = graph(3) 
g1.addEdge(0,1) 
g1.addEdge(1,2) 
  
  
if g1.isCyclic(): 
    print("Graph contains cycle")
else : 
    print("Graph does not contain cycle ")

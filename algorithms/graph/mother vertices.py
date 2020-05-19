'''
    bekar method hai not flexible 
    dont use this one 
     

'''
from collections import defaultdict
class graph:


    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)


    def addEdge(self, x, y):
        self.graph[x].append(y)
        self.graph[y] = self.graph[y]


    def __dfs(self, root, visited):
        visited[root] = True
        for i in self.graph[root]:
            if visited[i] == False:
                self.__dfs(i, visited)
    
    def find_mother(self):
        visited = [False]*self.V
        v=0
        for i in range(self.V):
            if visited[i] == False :
                self.__dfs(i,visited)
                v=i
        
        visited = [False]*self.V
        self.__dfs(v,visited)
        
        if any(i == False for i in visited):
            return -1
        return v



g = graph(7) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(4, 1) 
g.addEdge(6, 4) 
g.addEdge(5, 6) 
g.addEdge(5, 2) 
g.addEdge(6, 0) 

print(str(g.find_mother()))
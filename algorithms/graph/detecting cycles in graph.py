'''


In this we find the cycles present in the graph
here in this example we have the hava a graph of size 4 
having graph and edge like this 

{   
    edges       branches
    0       :   [1, 2], 
    1       :   [2], 
    2       :   [0, 3], 
    3           [3]
}
in this graph a cycle is present form 

    0 --->  1   ---> 2 ----> 0 the first cycle
    2 --->  0   ---> 1 ----> 2 the second cycle
    3 --->  3                   the third cycle

    hence output is loop present there

'''

from collections import defaultdict

class graph:
    def __init__(self,le):
        self.V=le
        self.graph=defaultdict(list)

    def addEdge(self,x,y):
        self.graph[x].append(y)
        self.graph[y]=self.graph[y]
    
    def __helperfunction(self,root,visited,recStack):
        visited[root]=True
        recStack[root]=True
        for i in self.graph[root]:
            if visited[i]== False:
                if self.__helperfunction(i,visited,recStack) == True:
                    return True
            if recStack[root]==True :
                return True
        
        recStack[root]=False
        return False
    def isCyclic(self):
        visited=[False]*self.V
        recStack=[False]*self.V
        for i in range(self.V):
            if visited[i]==False:
                if self.__helperfunction(i,visited,recStack)==True:
                    return True
        return False
    def printgraph(self):
        print(dict(self.graph))
            
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

g.printgraph()

           

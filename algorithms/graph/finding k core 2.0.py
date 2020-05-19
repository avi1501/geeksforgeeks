from collections import defaultdict

class graph:
    def __init__(self,le):
        self.V=le
        self.graph=defaultdict(list)
    
    def addEdge(self,a,b):
        self.graph[a].append(b)
        self.graph[b].append(a)
    
    def __dfs(self,root,visited,vdegree,k):
        visited[root]=True
        for i in self.graph[root]:
            if vdegree[root] < k:
                vdegree[i]=vdegree[i]-1
            
            if visited[i]==False:
                if(self.__dfs(i,visited,vdegree,k)):
                    visited[root] = visited[root]-1
        return vdegree[root]<k

    def printKCores(self,k):
        visited=[False]*self.V
        vdegree=[9]*self.V
        for i in self.graph:
            vdegree[i]=len(self.graph[i])
        
        self.__dfs(0,visited,vdegree,k)

        for i in range(self.V):
            if visited[i]==False:
                self.__dfs(i,visited,vdegree,k)
        
        print('k core of the nodes')
        for i in range(self.V):
            if(vdegree[i]>=k):
                print('['+str(i)+']',end="")
                for j in self.graph[i]:
                    if vdegree[j] >= k:
                        print('-->'+str(j),end=" ")
            print()

k = 3; 
g1 = graph (9); 
g1.addEdge(0, 1) 
g1.addEdge(0, 2) 
g1.addEdge(1, 2) 
g1.addEdge(1, 5) 
g1.addEdge(2, 3) 
g1.addEdge(2, 4) 
g1.addEdge(2, 5) 
g1.addEdge(2, 6) 
g1.addEdge(3, 4) 
g1.addEdge(3, 6) 
g1.addEdge(3, 7) 
g1.addEdge(4, 6) 
g1.addEdge(4, 7) 
g1.addEdge(5, 6) 
g1.addEdge(5, 8) 
g1.addEdge(6, 7) 
g1.addEdge(6, 8) 
g1.printKCores(k) 

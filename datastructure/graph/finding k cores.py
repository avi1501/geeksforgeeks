'''
finding k cores in the 
graph of we are using k here the graph of edges 
graph used in this is bidrectional(means edges can go in both directions)

i cant draw full graph here but i will provide all the edges connected with each other

{   vertex  Edges
     0:     [1, 2],
     1:     [0, 2, 5],
     2:     [0, 1, 3, 4, 5, 6], 
     5:     [1, 2, 6, 8], 
     3:     [2, 4, 6, 7], 
     4:     [2, 3, 6, 7], 
     6:     [2, 3, 4, 5, 7, 8], 
     7:     [3, 4, 6],
     8:     [5, 6]
}

the answer of the following when k=3

[2] -> 3 -> 4 -> 6
[3] -> 2 -> 4 -> 6 -> 7
[4] -> 2 -> 3 -> 6 -> 7
[6] -> 2 -> 3 -> 4 -> 7
[7] -> 3 -> 4 -> 6

these nodes having the degree of 3 and more than 3


'''



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
            
            if vdegree[root]<k :
                vdegree[i] = vdegree[i]-1

            if visited[i]==False:
                if self.__dfs(i,visited,vdegree,k):
                    visited[root] = visited[root]-1
        
        return vdegree[root]<k

    def printKCores(self,k):
        visited=[False]*self.V
        vdegree=[0]*self.V
        for i in self.graph:
            vdegree[i]=len(self.graph[i])
        self.__dfs(0,visited,vdegree,k)

        for i in range(self.V):
            if(visited[i]==False):
                self.__dfs(i,visited,vdegree,k)
        
        print('/n k cores if the graph is ')
        for i in range(self.V):
            if(vdegree[i]>=k):
                print('['+str(i)+']',end=" ")
                for j in self.graph[i]:
                    if(vdegree[j]>=k):
                        print("-> "+str(j), end=" ")
                print()
        
    def graph_print(self):
        print(dict(self.graph))

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
g1.graph_print()
from collections import defaultdict
class graph:
    def __init__(self,size):
        self.V=size
        self.graph=defaultdict(list)
    def addEdge(self,x,y):
        self.graph[x].append(y)
        self.graph[y]=self.graph[y]

    def __dfs(self,root,visited):
        visited[root]=True
        for i in self.graph[root]:
            if(visited[i]==False):
                self.__dfs(i,visited)
    
    def find_mother(self):
        visited=[False]*self.V
        v=0
        for i in range(self.V):
            if visited[i] == False:
                self.__dfs(i,visited)
                v=i
        visited=[False]*self.V
        self.__dfs(v,visited)
        if any(i==False for i in visited):
            return -1
        else:
            return v
    
    def count_mother_node(self):
        counter=0
        for i in range(self.V):
            visited=[False]*self.V
            self.__dfs(i,visited)
            if any(i==False for i in visited):
                continue
            else:
                counter += 1
        print(counter)
            

g = graph(5) 
g.addEdge(0, 2) 
g.addEdge(0, 1) 
g.addEdge(1, 3) 
g.addEdge(1, 4) 
g.addEdge(2, 3) 
g.addEdge(3, 4)
g.addEdge(2, 0) 

print("Mother of the graph is "+str(g.find_mother()))

print("total no of mother in this graph is ",end="")
g.count_mother_node()


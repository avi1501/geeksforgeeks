from collections import defaultdict
class graph:
    def __init__(self,v):
        self.V = v
        self.graph = defaultdict(list)
    
    def addEdge(self,a,b):
        self.graph[a].append(b)
        self.graph[b]=self.graph[b]
    
    def __helperfunction(self,root,visited,reach,stack):
        visited[root] = True
        for i in self.graph[root]:
            if visited[i] == False:
                self.__helperfunction(i,visited,reach,stack)
            reach[root] = max(reach[root],reach[i]+1)
        stack.append(root)
            
    
    def longestpathsize(self,start):
        visited=[False]*self.V
        stack=[]
        reach=[0]*self.V
        for i in range(self.V):
            if visited[i] == False:
                self.__helperfunction(i,visited,reach,stack)
        stack = stack[:stack.index(start)+1]
        while(stack):
            u = start
            print(u,end=" ")
            stack.remove(start)
            # removing duplicates from stack
            # having same distance in reach array
            for i in stack:
                if reach[start] <=reach[i]:
                    stack.remove(i)
            # if still stack present then assign 
            # minimum value to it
            if stack:
                start = stack[0]
            # iterate over loop and find the maximum
            #  length element and assign to start
            for i in self.graph[u]:
                if reach[i] >= reach[start]:
                    start = i
    
        return max(reach)


    def printgraph(self):
        print(dict(self.graph))
    
    



graph=graph(5)
graph.addEdge(0,2)
graph.addEdge(0,3)
graph.addEdge(1,3)
graph.addEdge(1,2)
graph.addEdge(3,2)
graph.addEdge(4,0)
graph.addEdge(4,1)
graph.addEdge(4,2)
graph.printgraph()

size=graph.longestpathsize(1)



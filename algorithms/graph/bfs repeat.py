from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def add_edge(self,x,y):
        self.graph[x].append(y)
        self.graph[y]=self.graph[y]
    
    def breadth_first_search(self,root):
        visited=[False]*len(self.graph)
        queue=[]
        queue.append(root)
        visited[root]=True

        while(queue):
            no=queue.pop(0)
            print(no,end=' ')
            for i in self.graph[no]:
                if visited[i] == False:
                    visited[i]=True
                    queue.append(i)
        print()
    
    def __dfs(self,root,visited):
        visited[root]=True
        print(root,end=" ")
        for i in self.graph[root]:
            if(visited[i]==False):
                self.__dfs(i,visited)

    def depth_first_search(self,root):
        visited=[False]*len(self.graph)
        self.__dfs(root,visited)
        print()


grph=graph()
grph.add_edge(0,1)
grph.add_edge(0,2)
grph.add_edge(1,2)
grph.add_edge(2,0)
grph.add_edge(2,3)
grph.add_edge(3,3)
grph.add_edge(1,0)
grph.add_edge(2,1)
grph.add_edge(3,2)
grph.add_edge(3,4)
grph.add_edge(4,5)

print("\nbreadth first search")
grph.breadth_first_search(2)
print('\ndepth first search')
grph.depth_first_search(2)



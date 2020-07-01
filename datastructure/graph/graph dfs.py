'''
This is an example of depth first search of the directed graph
In directed graph you have access to on way from a node though 
it can have multiple branch 

In the depth first search we first explore only one branch till it reaches to end 
then we move on to next node to explore it to last and repeat for all others 

these are the branches from the nodes 
    
    {   
        nodes   Branches 
         0:      [1, 2],
         1:      [2, 0], 
         2:      [0, 3, 1], 
         3:      [3, 2, 4], 
         4:      [5], 
         5:      []
    }
    taking "2" as head pointer the tracing 
    this as breadth first search
    
    answer-->   2 0 1 3 4 5
                

'''




from collections import defaultdict

class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    

    def add_edge(self,a,b):
        self.graph[a].append(b)
        self.graph[b]=self.graph[b]
    

    def print_adjacency_list(self):
        print(dict(self.graph))
    

    def DFSUtill(self,root,visited):
        visited[root]=True
        print(root,end=" ")
        for i in self.graph[root]:
            if(visited[i]==False):
                self.DFSUtill(i,visited)
    

    def depth_first_search_traversal(self,root):
        visited=[False]*len(self.graph)
        self.DFSUtill(root,visited)
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


grph.depth_first_search_traversal(2)

grph.print_adjacency_list()
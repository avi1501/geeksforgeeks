'''
This is an example of breadth first search of the directed graph
In directed graph you have access to on way from a node though 
it can have multiple branch 

in the breadth first search we first explore all the adjacent nodes 
then we move on to next node to explore to all its nodes 

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
    
    answer-->   2 0 3 1 4 5
                

'''


from collections import defaultdict


class graph:
        
    def __init__(self):
        self.graph=defaultdict(list)

    def add_edge(self,a,b):
        self.graph[a].append(b)
        self.graph[b]=self.graph[b] 


    def graph_size(self):
        print(len(self.graph))
    
    def print_adjacency_list(self):
        print(dict(self.graph))

    def breadth_first_search_traversal(self,head):
        queue=[]
        visited=[False]*len(self.graph)
        visited[head]=True
        queue.append(head)
        while(queue):
            s=queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if(visited[i]==False):
                    queue.append(i)
                    visited[i]=True
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


grph.breadth_first_search_traversal(2)

grph.print_adjacency_list()



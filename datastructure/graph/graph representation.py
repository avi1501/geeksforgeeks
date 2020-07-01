#adjacency list

class Node:
    def __init__(self,x):
        self.vertex=x
        self.next=None

class graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[None]*self.v

    #adding branches  
    def add_edge(self,src,dest):
        #adding the node to source node
        node=Node(dest)
        node.next=self.graph[src]
        self.graph[src]=node

        #adding node to destination node
        #as it is an undirected graph
        node=Node(src)
        node.next=self.graph[dest]
        self.graph[dest]=node

        #function to print graph

    def print_graph(self):
        for i in range(self.v):
            print("Adjcency list of vertex {}\n head".format(i),end="")
            temp=self.graph[i]
            while temp:
                print(" - {}".format(temp.vertex),end="")
                temp=temp.next
            print(" \n")

mygraph=graph(6)
mygraph.add_edge(1,2)
mygraph.add_edge(1,3)
mygraph.add_edge(2,4)
mygraph.add_edge(2,5)
mygraph.add_edge(4,4)
mygraph.add_edge(4,5)
mygraph.print_graph()


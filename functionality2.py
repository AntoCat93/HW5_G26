from collections import defaultdict 
  
#Creating a class to represent a graph 
class graph: 
  
    def __init__(self,vertices): 
        self.V= vertices #this is the number of vertices 
        self.graph = []  #creating default dictionary to store the graph
          
   
    # this is a function to add an edge to graph 
    def addEdge(self,a,b,c): 
        self.graph.append([a,b,c]) 
  
    # this is a function to find set of an element i 
    def find(self, prev, i): 
        if prev[i] == i: 
            return i 
        return self.find(prev, prev[i]) 
  
    # A function that does union of two sets of x and y 
    def union(self, prev, rank, x, y): 
        x_root = self.find(prev, x) 
        y_root = self.find(prev, y) 
  
        # Attach smaller rank tree under root of high rank tree
        if rank[x_root] < rank[y_root]: 
            prev[x_root] = y_root 
        elif rank[x_root] > rank[y_root]: 
            prev[y_root] = x_root 
  
        # If ranks are same, then make one as root and increase rank by one
        else : 
            prev[y_root] = xroot 
            rank[x_root] += 1
  
    # this is the function of minimum spanning tree using kruskal's algorithm
    def KruskalMST(self): 
  
        result =[] #list which will store the results
  
        i = 0 # An index variable, used for sorted edges 
        j = 0 # An index variable, used for result[] 
  
            # Step 1:  Sort all the edges in non-decreasing  
                # order of their 
                # weight.  If we are not allowed to change the  
                # given graph, we can create a copy of graph 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
  
        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        # Number of edges to be taken is equal to V-1 
        while j < self.V -1 : 
  
            # Step 2: Pick the smallest edge and increment  
                    # the index for next iteration 
            a,b,c =  self.graph[i] 
            i = i + 1
            x = self.find(prev, a) 
            y = self.find(prev ,b) 
  
            # If including this edge does't cause cycle,  
                        # include it in result and increment the index 
                        # of result for next edge 
            if x != y: 
                j = j + 1     
                result.append([a,b,c]) 
                self.union(prev, rank, x, y)             
            # Else discard the edge 
        for a,b,c  in result: 
            print ("%d -- %d == %d" % (a,b,c)) 

# -*- coding: utf-8 -*-

##########################################
# Weighted graphs

class Digraph():
    """
    Directed weighted graph.
    
    edges is a dictionary mapping each node to a edges starting from it
        key: node; value: dictionary of edges starting from that node
            value dictionary: key: end node of edge, value: weight (cost) of the edge
    """
    def __init__(self, adj_list=None):
        """
        Initialize either empty graph or one from a dictionary adjacency list
        """
        self.edges = {}
        self.num_edges = 0
        if isinstance(adj_list, dict):
            for src, values in adj_list.items():
                for dest, weight in values.items():
                    self.add_edge(src, dest, weight)
    
    def add_node(self,node):
        # Adds a vertex to graph (based on key value)       
        self.edges[node] = dict()

    def add_edge(self,src,dest,weight):
        # Adds the (v,w) edge, making sure the two nodes exist
        if not self.has_node(src): 
            self.add_node(src)
        if not self.has_node(dest): 
            self.add_node(dest)
        if not self.has_edge(src, dest):
            self.num_edges += 1
            self.edges[src][dest] = weight
  
    def children_of(self, v):
        # Returns a node's children
        return self.edges[v].items()
    
    def get_nodes(self):
        # Returns a node's children
        return self.edges.keys()
        
    def has_node(self, v):
        # Checks if node exists
        return v in self.edges
        
    def has_edge(self, v, w):
        # Checks if edge exists
        return w in self.edges[v]

    def list_edges(self):
        # Creates list of edges
        ll = []
        for src,values in self.edges.items():
            for dest,weight in values.items():
                ll.append([src,dest,weight])
        return ll
    
    def __str__(self):
        # Returns a string representation of the graph
        result = ''
        for src in self.edges:
            for dest,weight in self.edges[src].items():
                result = result + src + '->'\
                         + dest + ', length ' + str(weight) + '\n'
        return result[:-1] # omit final newline


 
class Graph(Digraph):
    """ 
    Undirected graph: two one-way edges for every edge
    """
    def add_edge(self, src, dest,weight):
        Digraph.add_edge(self, src, dest, weight)
        Digraph.add_edge(self, dest, src, weight)



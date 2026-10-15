import graphs as gs
from graph_weighted import lecture_graph

######
# Solving the problem the easy way with the networkx module

import networkx as nx

def create_lecture_graph_networkx():
    """
    Returns lecture graph as networkx graph object
    """
    distances = {
        'a': {'b': 1, 'c': 5},
        'b': {'c': 2, 'd': 5},
        'c': {'d': 2, 'e': 6},
        'd': {'e': 2},
        'e': {}
        }
    
    G = nx.Graph()
    for src, edges in distances.items():
        for dest, w in edges.items():
            G.add_edge(src, dest, weight=w)
    return G

G = create_lecture_graph_networkx()
shortest_dists = nx.single_source_dijkstra_path_length(G, 'a')
all_shortest_dists = nx.all_pairs_dijkstra_path_length(G)






#####
# Dijkstra with a heap queue

import heapq as hq

def dijkstra_heap(graph,start):
    """
    Dijkstra's algorithm with a heap 
    
    Since we don't have a quick deletion from heap, we add everything to heap "lazily".
    That is, if we find a lower Dijkstra score than previously, we don't replace the old one.
    We just add the new one, which will have priority over the old one as the score is lower.
    
    This means the heap may contain the same node several times with different Dijkstra scores.
    This is not a problem for correctness since the heap is ordered by the score.
    But we need to stop the algorithm with the break command after we visit all nodes.
    
    Parameters:
        graph: a Graph (or Digraph) 
        start: starting node for the algorithm
    Returns: 
        dists: dictionary containing shortest distances to all nodes
        prev_nodes: dictionary containing the previous node from which each node was explored
                None for the starting node
    
    Examples:
    >>> graph = gs.Digraph(lecture_graph())
    >>> dists, prev_nodes = dijkstra_heap(graph, 'a')
    >>> [dists['b'], dists['e'], dists['c'], dists['d']]
    [1, 7, 3, 5]
    >>> [prev_nodes['a'], prev_nodes['e'], prev_nodes['c'], prev_nodes['d']]
    [None, 'd', 'b', 'c']
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    
    X = set()
    A = dict()
    prev_nodes = dict()
    for src in graph.get_nodes(): # initialize like above
        A[src] = float('Inf')
        prev_nodes[src] = None
    
    A[start] = 0
    
    # Initialize heap queue as (distance, name) tuples
    Q = [(v, k) for k, v in A.items()]   
    hq.heapify(Q) # this initializes the heap queue: the priority ordering is by v, ie the Dijkstra score

     
    while len(Q) > 0:
        if len(X) == len(graph.edges.items()): 
            break # stop if visited every node
        
        dist, vertex = hq.heappop(Q) # get node with best priority Dijkstra score (extract-min from heapq)
        # code: add vertex node to X
        
        for dest, weight in graph.children_of(vertex):
            if ...: # condition: check if dest has been visited
                if ... :# condition: then check if Dijkstra score of destination
                    # code: update Dijkstra score
                    # code: update prev_nodes
                    # code: use hq.heappush(Q,(new_score,dest)) to insert into heap queue
                    pass


#####
# Generate random graphs from list of nodes for comparison purposes

# Generate a random graphs
import random
def random_graph(nodes, n_edges):
    g = gs.Digraph()
    
    #n_edges = 50 # max number of edges
    max_weight = 20  
    n_nodes = len(nodes)
    
    connected = set()
    connected.add(nodes[0])
    
    edg = n_edges
    for i in range(1,n_nodes):
        # make sure graph is connected by adding an edge from each node to an already connected node
        r = random.randint(0, i-1)
        weight = random.randint(1, max_weight)
        g.add_edge(nodes[i], nodes[r], weight)
        edg -= 1
      
    # Add rest of edges
    for u in range(edg):
        i = random.randint(0, n_nodes-1)
        j = random.randint(0, n_nodes-1)
        weight = random.randint(1, max_weight)
        g.add_edge(nodes[i], nodes[j], weight)
    
    return g
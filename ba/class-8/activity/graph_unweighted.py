# This command imports data structures in ses08_data_structures.py
# It will only work if the ses08_data_structures.py file is in the same directory
from aux_data_structures import Graph, Digraph, Queue, QueueNode




def create_bfs_graph():
    """
    Initializes the undirected graph from the lecture
    
    Uses the add_edge method
    
    Returns Graph object of the lecture graph
    Example use:
    >>> ex_graph = create_bfs_graph()
    >>> [x in ex_graph.children_of('Jared') for x in ['John', 'Helena', 'Donald', 'Paul']]
    [False, False, True, True]
    >>> ex_graph = create_bfs_graph()
    >>> [x in ex_graph.children_of('Helena') for x in ['John', 'Helena', 'Donald', 'Paul']]
    [True, False, False, True]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    g = Graph()
    g.add_edge('John', 'Helena')
    g.add_edge('John', 'Chris')
    g.add_edge('Helena', 'Chris')
    g.add_edge('Helena', 'Paul')
    g.add_edge('Chris','Vicki')
    g.add_edge('Paul', 'Jared')
    g.add_edge('Vicki', 'Jared')
    g.add_edge('Jared', 'Donald')    
    return g

g = create_bfs_graph()

print(g)

def bfs(graph, start):
    """ 
    Breadth-first search using Queue data structure
    
    Parameter: 
        graph (Digraph/Graph), 
        start: starting node in the graph
    
    Returns:
        dists, a dictionary of distances to all explored vertices:
            key - node, value - distance from start to that node
        
    Example use:
    >>> ex_graph = create_bfs_graph()
    >>> bfs_dists = bfs(ex_graph, 'John')
    >>> [bfs_dists['Donald'], bfs_dists['Jared']]
    [4, 3]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    
    # Keep track of queue of nodes to explore next
    q = Queue() # Initialize an empty queue
    q.enqueue(start) # add start to queue
    
    # Keep track of explored nodes
    explored = set() # Initialize explored nodes as an empty set
    explored.add(start) # Mark starting node explored
    
    # Keep track of distances from start to all other nodes
    dists = dict() # Initialize distances as an empty dictionary
    dists[start] = 0 # Zero distance from start node to itself
    
    # Main loop
    while not q.is_empty(): # Loop while queue not empty
        v = q.dequeue() # Pop the first item from the queue 
        # Explore all adjacent nodes of v
        for w in graph.children_of(v): # loop through adjacent nodes
            if w not in explored: # If w not explored yet
                explored.add(w) # Mark w explored
                dists[w] = dists[v] + 1 # Calculate distance from start to w based on v's distance
                q.enqueue(w) # Add w to queue to explore from in the future
    return dists


def bfs_track_path(graph, start):
    """ 
    Breadth-first search using Queue data structure, keeping track of paths
    
    Parameter: 
        graph (Digraph/Graph), 
        start: starting node in the graph
    
    Returns:
        dists, a dictionary of distances to all explored nodes:
            key - node, value - distance from start to that node 
        prev_nodes, a dictionary containing the previous node on the path to each node:
            key - node, value - the node from which we found this node; None for starting node
        
    Example use:
    >>> ex_graph = create_bfs_graph()
    >>> bfs_dists, prev_nodes = bfs_track_path(ex_graph, 'John')
    >>> [prev_nodes['Donald'], prev_nodes['Helena'], prev_nodes['John']]
    ['Jared', 'John', None]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    q = Queue() # Initialize an empty queue
    q.enqueue(start) # add start to queue
    
    # Keep track of explored nodes
    explored = set() # Initialize explored nodes as an empty set
    explored.add(start) # Mark starting node explored
    
    # Keep track of distances from start to all other nodes
    dists = dict() # Initialize distances as an empty dictionary
    dists[start] = 0 # Zero distance from start node to itself
    
    # Keep track of the parent for each node
    prev_nodes = dict()
    prev_nodes[start] = None
    
    # Main loop
    while not q.is_empty(): # Loop while queue not empty
        v = q.dequeue() # Pop the first item from the queue 
        # Explore all adjacent nodes of v
        for w in graph.children_of(v): # loop through adjacent nodes
            if w not in explored: # If w not explored yet
                explored.add(w) # Mark w explored
                prev_nodes[w] = v
                dists[w] = dists[v] + 1 # Calculate distance from start to w based on v's distance
                q.enqueue(w) # Add w to queue to explore from in the future
    return dists, prev_nodes


def print_path(prev_nodes, v):
    """ 
    Based on dictionary prev_nodes containing links to previous nodes, 
    prints out path from starting node to v.
    """
    
    path_list = []
    while v is not None:
        path_list.append(v)
        v = prev_nodes[v]
    
    path_list = reversed(path_list)    
    path = ' -> '.join(path_list)
    print(path)

##### 
# Small worlds and Kevin Bacon

def read_movie_data(filename, delimiter='/'):
    """ 
    Reads movie data from text file into a graph data structure
    
    Reads each line as connections from first instance of line to other instances
    Assumes file is delimited by '/' by default
    
    Returns Graph object
    """
    graph = Graph()
    with open(filename, "r", encoding="utf8") as ins:
        for line in ins:
            names = line.split(delimiter)
            start_node = names[0]
            for end_node in names[1:]:
                graph.add_edge(start_node, end_node)
    return graph


def print_children(graph, v=None):
    """
    Prints out children nodes of v in graph.
    """
    if v == None:
        v = input('Enter name: ')
    print(v)
    if graph.has_node(v):
        for w in graph.children_of(v):
            print('  ' + w)


def kevin_bacon_distance(filename, actor):
    """
    Computes the BFS distance from Kevin Bacon to actor in the movie graph
    built from the data in filename.

    Uses read_movie_data to build the graph and your own bfs function to
    find the distance. Note this counts each hop actor -> movie -> actor as
    two edges, so the actual "Bacon number" is half of this raw distance.

    Parameters:
        filename: path to a movie data file (see read_movie_data)
        actor: name of the actor, e.g. 'Kidman, Nicole'

    Returns:
        the BFS distance (int) from 'Bacon, Kevin' to actor

    Example use:
    >>> kevin_bacon_distance('data/movies.txt', 'Kidman, Nicole')
    4
    >>> kevin_bacon_distance('data/movies.txt', 'Brando, Marlon')
    4
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    graph = read_movie_data(filename, '/')
    dists = bfs(graph,'Bacon, Kevin')
    return dists[actor]

print(kevin_bacon_distance('data/movies.txt', 'Brando, Marlon'))

  
    

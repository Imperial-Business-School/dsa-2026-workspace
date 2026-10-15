
class Digraph(object):
    """ 
    Directed graph
    
    edges is a dict mapping each node to a set of its children nodes
    num_edges is the total number of edges in the graph
    """
    def __init__(self):
        self.edges = {}
        self.num_edges = 0
    
    def add_node(self,node):
        """
        Adds a node to graph (based on key value)       
        """
        self.edges[node] = set()

    def add_edge(self,src,dest):
        """ 
        Adds the (v,w) edge, making sure the two nodes exist
        """
        if not self.has_node(src): 
            self.add_node(src)
        if not self.has_node(dest): 
            self.add_node(dest)
        if not self.has_edge(src, dest):
            self.num_edges += 1
            self.edges[src].add(dest)
            
    def children_of(self, v):
        """
        Returns a node's children
        """
        return self.edges[v]
        
    def has_node(self, v):
        """ 
        Checks whether the node is in graph already
        """
        return v in self.edges
        
    def has_edge(self, v, w):
        """
        Checks whether there is an edge from v to w
        """
        return w in self.edges[v]
        
    def __str__(self):
        """
        String representation of graph
        """
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src + '->'\
                         + dest + '\n'
        return result[:-1] # omit final newline


class Graph(Digraph):
    """ 
    Undirected graph: two one-way edges for every added edge
    """
    def add_edge(self, src, dest):
        Digraph.add_edge(self, src, dest)
        Digraph.add_edge(self, dest, src)


class QueueNode(object):
    """ 
    QueueNode: contains unspecified data in stuff and link to next QueueNode
    """
    def __init__(self, stuff=None, next=None):
        self.stuff = stuff
        self.next = next

    def __str__(self):
        return str(self.stuff)    
 
    
class Queue(object):
    """ 
    Queue using linked QueueNodes
    Supports inserting and deleting nodes via enqueue and dequeue
    """
    def __init__(self):
        """
        Initialise empty queue
        Keep track of both first and last node
        """
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, stuff):
        """
        Inserts node into the end of the queue
        """
        node = QueueNode(stuff)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1

   
    def dequeue(self):
        """
        Returns first node of the queue (removes it from queue)
        """
        removed = self.first.stuff
        self.first = self.first.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return removed

    def is_empty(self):
        """
        Returns True if queue is empty, False otherwise.
        """
        return self.length == 0
    
    def __str__(self):
        """
        Returns queue representation string
        """
        s = ''
        item = self.first
        while item is not None:
            s += str(item.stuff) + ' '
            item = item.next
        return s
        
    def __len__(self):
        """
        Returns queue length
        """
        return self.length
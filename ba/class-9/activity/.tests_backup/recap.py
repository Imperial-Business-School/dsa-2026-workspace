test = {
  'name': 'Recap',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> L = ['mouse', 'cat', 'dog', 'mouse', 'bird', 'cow', 'cow', 'cow']
          >>> s = set(L)
          >>> len(s)
          b6327f4a1a929de83704ea31cd99a369
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = 'Hey you'
          >>> s = set(x)
          >>> len(s)
          853c1ea1f09047f7154bba064ad306e4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> s.update('hey')
          >>> len(s)
          cb94d8dc0a87951e729160f69ccfcbfd
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> s = {'bird', 'cat', 'cow', 'dog', 'mouse'}
          >>> L  = ['mouse', 'moose', 'dog', 'moose', 'mouse', 'moosemouse']
          >>> count = 0
          >>> for item in L:
          ...     if item in s:
          ...         count += 1
          >>> count
          b85586dbbec62d9e97b5dd3e9dd36d7b
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> class Digraph(object):
          ...    def __init__(self):
          ...        self.edges = {}
          ...        self.num_edges = 0
          ...      
          ...    def add_node(self,node):
          ...        # Adds a node to graph (based on key value)       
          ...        self.edges[node] = set()
          ...    def add_edge(self,src,dest):
          ...        # Adds the (v,w) edge, making sure the two nodes exist
          ...        if not self.has_node(src): 
          ...            self.add_node(src)
          ...        if not self.has_node(dest): 
          ...            self.add_node(dest)
          ...        if not self.has_edge(src, dest):
          ...            self.num_edges += 1
          ...            self.edges[src].add(dest)
          ...    def children_of(self, v):
          ...        # Returns a node's children
          ...        return self.edges[v]
          ...    def has_node(self, v):
          ...        # Checks whether the node is in graph already
          ...        return v in self.edges
          ...    def has_edge(self, v, w):
          ...        # Checks whether there is an edge from v to w
          ...        return w in self.edges[v]
          >>> Z = Digraph()
          >>> Z.add_edge('Grandad', 'Dad')
          >>> Z.add_edge('Grandad', 'Uncle Sam')
          >>> Z.add_edge('Dad', 'Me')
          >>> Z.add_edge('Dad', 'John')
          >>> len(Z.children_of('Grandad'))
          da17f6968ec95643697270c04033b6ec
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'type': 'wwpp'
    }
  ]
}

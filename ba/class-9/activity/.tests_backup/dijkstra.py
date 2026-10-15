test = {
  'name': 'dijkstra',
  'points': 40,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> graph = gs.Digraph(lecture_graph())
          >>> dists, prev_nodes = dijkstra(graph, 'a')
          >>> [dists['b'], dists['e'], dists['c'], dists['d']]
          [1, 7, 3, 5]
          >>> [prev_nodes['a'], prev_nodes['e'], prev_nodes['c'], prev_nodes['d']]
          [None, 'd', 'b', 'c']
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import graphs as gs
      >>> from graph_weighted import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

test = {
  'name': 'bfs',
  'points': 20,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ex_graph = create_bfs_graph()
          >>> bfs_dists = bfs(ex_graph, 'John')
          >>> [bfs_dists['Donald'], bfs_dists['Jared']]
          [4, 3]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from graph_unweighted import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

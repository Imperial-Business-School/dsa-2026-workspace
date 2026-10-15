test = {
  'name': 'bfs_track_path',
  'points': 20,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ex_graph = create_bfs_graph()
          >>> bfs_dists, prev_nodes = bfs_track_path(ex_graph, 'John')
          >>> [prev_nodes['Donald'], prev_nodes['Helena'], prev_nodes['John']]
          ['Jared', 'John', None]
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

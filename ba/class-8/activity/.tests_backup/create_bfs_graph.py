test = {
  'name': 'create_bfs_graph',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ex_graph = create_bfs_graph()
          >>> [x in ex_graph.children_of('Jared') for x in ['John', 'Helena', 'Donald', 'Paul']]
          [False, False, True, True]
          >>> ex_graph = create_bfs_graph()
          >>> [x in ex_graph.children_of('Helena') for x in ['John', 'Helena', 'Donald', 'Paul']]
          [True, False, False, True]
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

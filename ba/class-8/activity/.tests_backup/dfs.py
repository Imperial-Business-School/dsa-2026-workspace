test = {
  'name': 'dfs',
  'points': 20,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> lec_graph = create_dfs_graph()
          >>> dfs_paths, pop_order = dfs(lec_graph, 'John')
          >>> abs(pop_order['Chris'] - pop_order['Helena']) > 1
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from graph_unweighted_extra import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

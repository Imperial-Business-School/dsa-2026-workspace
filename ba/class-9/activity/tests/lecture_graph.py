test = {
  'name': 'lecture_graph',
  'points': 20,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> adj_list = lecture_graph()
          >>> adj_list['d']['e']
          2
          >>> 'd' in adj_list['e']
          False
          >>> [adj_list[n][m] for n in 'abcde' for m in 'abcde' if m in adj_list[n]]
          [1, 5, 2, 5, 2, 6, 2]
          >>> [len(adj_list[n]) for n in 'abcde']
          [2, 2, 2, 1, 0]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from graph_weighted import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

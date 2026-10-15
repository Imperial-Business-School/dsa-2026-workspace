test = {
  'name': 'kevin_bacon_distance',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> kevin_bacon_distance('data/movies.txt', 'Kidman, Nicole')
          4
          >>> kevin_bacon_distance('data/movies.txt', 'Brando, Marlon')
          4
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

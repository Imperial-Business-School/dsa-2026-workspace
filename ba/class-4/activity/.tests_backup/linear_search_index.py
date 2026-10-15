test = {
  'name': 'linear_search_index',
  'points': 14,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> linear_search_index([1, 3, 9, 4, 5, 6], 6)
          5
          >>> linear_search_index([1, 3, 9, 4, 5, 6], 2)
          -1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from complexity_search import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

test = {
  'name': 'binary_search_count',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> binary_search_count([1, 3, 4, 5], -1)
          (False, 2)
          >>> binary_search_count([1, 3, 4, 5, 6, 6, 7], 5)
          (True, 1)
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

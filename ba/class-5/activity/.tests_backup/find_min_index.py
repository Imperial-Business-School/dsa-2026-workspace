test = {
  'name': 'find_min_index',
  'points': 14,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> find_min_index([1, 2, 5, -1], 0)
          3
          >>> find_min_index([1, 1, 1, 5, 9], 2)
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from sorting import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

test = {
  'name': 'longest_sorted',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> longest_sorted([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 13, 15, 3, 11, 7, 5])
          [1, 9, 13, 15]
          >>> longest_sorted([25, 72, 31, 32, 8, 20, 38, 43, 85, 39, 33, 40, 98, 37, 14])
          [8, 20, 38, 43, 85]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from complexity_search_extra import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

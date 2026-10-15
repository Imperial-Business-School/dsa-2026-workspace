test = {
  'name': 'check_sorted',
  'points': 14,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> check_sorted([3, 6, 48, 24, 51, 262, 119])
          False
          >>> check_sorted([748, 623, 424, 414, 74, 2])
          True
          >>> check_sorted([1, 2, 3])
          True
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

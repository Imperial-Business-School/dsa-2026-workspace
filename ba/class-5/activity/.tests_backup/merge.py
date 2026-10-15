test = {
  'name': 'merge',
  'points': 14,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> left = [1, 5, 6]
          >>> right = [2, 3, 4]
          >>> merge(left, right)
          [1, 2, 3, 4, 5, 6]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from sorting_extra import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

test = {
  'name': 'selection_sort',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> selection_sort([3, 6, 8, 2, 78, 1, 23, 45, 9])
          [1, 2, 3, 6, 8, 9, 23, 45, 78]
          >>> selection_sort([1, 13, -23, 2.7, -3, 5, 7.5])
          [-23, -3, 1, 2.7, 5, 7.5, 13]
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

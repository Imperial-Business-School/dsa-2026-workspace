test = {
  'name': 'compare_mas',
  'points': 9,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p1 = [1, 2, 4, 5]
          >>> p2 = [0, 2.5, 5, 3]
          >>> compare_mas(p1, p2)
          [1, 0, 0, 1]
          >>> p1 = [None, 2.5, 3.5, 4.5, 4.5, 3.5, 2.5, 1.5, 3.5, 3.5]
          >>> p2 = [None, None, 3.0, 4.0, 4.33, 4.0, 3.0, 2.0, 3.0, 2.66]
          >>> compare_mas(p1, p2)
          [None, None, 1, 1, 1, 0, 0, 0, 1, 1]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hw_02 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

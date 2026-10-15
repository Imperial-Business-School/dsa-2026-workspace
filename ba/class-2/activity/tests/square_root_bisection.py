test = {
  'name': 'square_root_bisection',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> y, c = square_root_bisection(20)
          >>> print(y, c)
          4.47 9
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from algo_extra import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

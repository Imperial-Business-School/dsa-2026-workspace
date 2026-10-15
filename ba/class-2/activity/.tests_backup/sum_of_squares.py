test = {
  'name': 'sum_of_squares',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sum_of_squares(1, 2)
          5
          >>> sum_of_squares(100, 3)
          10009
          >>> sum_of_squares(-1, 0)
          1
          >>> x = sum_of_squares(2, 3)
          >>> x + 1
          14
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from algo import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

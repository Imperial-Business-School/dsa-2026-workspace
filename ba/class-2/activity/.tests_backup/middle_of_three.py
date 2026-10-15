test = {
  'name': 'middle_of_three',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> middle_of_three(5, 3, 4)
          4
          >>> middle_of_three(1, 1, 2)
          1
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

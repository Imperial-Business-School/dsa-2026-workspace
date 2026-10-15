test = {
  'name': 'print_grade',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> grade_high = 70
          >>> grade_low = 50
          >>> print_grade(20, grade_high, grade_low)
          fail
          >>> print_grade(61, 70, 50)
          pass
          >>> print_grade(90, 80, 60)
          distinction
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

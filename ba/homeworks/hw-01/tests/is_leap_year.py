test = {
  'name': 'is_leap_year',
  'points': 6,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> is_leap_year(2024)
          True
          >>> is_leap_year(2023)
          False
          >>> is_leap_year(1900)
          False
          >>> is_leap_year(2000)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hw_01 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

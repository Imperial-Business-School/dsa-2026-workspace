test = {
  'name': 'date_conversion',
  'points': 12,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(date_conversion('12/8/16'))
          08-12-2016
          >>> print(date_conversion('01/12/1898'))
          12-01-1898
          >>> print(date_conversion('11/5/25'))
          05-11-1925
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

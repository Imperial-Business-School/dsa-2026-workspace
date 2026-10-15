test = {
  'name': 'date_conversion_robust',
  'points': 22,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(date_conversion_robust('12/8/16'))
          08-12-2016
          >>> print(date_conversion_robust('1/12/1898'))
          12-01-1898
          >>> date_conversion_robust('1/1/25')
          '01-01-1925'
          >>> print(date_conversion_robust('16/3/2021'))
          Not a valid date. Did you mean to input 3/16/2021?
          None
          >>> print(date_conversion_robust('2/29/2017'))
          Not a valid date.
          None
          >>> print(date_conversion_robust('131/2/1928'))
          Not a valid date.
          None
          >>> print(date_conversion_robust(2))
          Not a valid date.
          None
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

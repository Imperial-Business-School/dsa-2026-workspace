test = {
  'name': 'wind_chill',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> wind_chill(10, 0)
          10
          >>> wind_chill(-10, 20)
          -18
          >>> wind_chill(-20, 30) + 1
          -32
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

test = {
  'name': 'weeks',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> weeks(20, 1)
          2
          >>> weeks(1, 21)
          2
          >>> weeks(1, 22)
          3
          >>> weeks(346, 281)
          9
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

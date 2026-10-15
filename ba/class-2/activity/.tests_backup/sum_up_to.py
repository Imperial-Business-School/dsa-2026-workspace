test = {
  'name': 'sum_up_to',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sum_up_to(1)
          1
          >>> sum_up_to(5)
          15
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

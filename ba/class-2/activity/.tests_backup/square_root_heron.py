test = {
  'name': 'square_root_heron',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> y, c = square_root_heron(20)
          >>> print(y, c)
          4.47 4
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

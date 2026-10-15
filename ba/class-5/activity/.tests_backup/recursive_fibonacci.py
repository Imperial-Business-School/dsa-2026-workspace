test = {
  'name': 'recursive_fibonacci',
  'points': 14,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> recursive_fibonacci(2)
          1
          >>> recursive_fibonacci(5)
          5
          >>> recursive_fibonacci(8)
          21
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from sorting_extra import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

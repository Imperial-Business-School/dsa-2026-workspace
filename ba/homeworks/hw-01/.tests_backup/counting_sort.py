test = {
  'name': 'counting_sort',
  'points': 6,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> counting_sort([98, 19, 29, 41, 9999, 73, 241, 1111, 53, 3, 333])
          [1111, 3, 333, 41, 241, 53, 73, 19, 29, 98, 9999]
          >>> counting_sort([999, 19, 919, 111, 119, 1199, 911])
          [111, 19, 119, 911, 919, 1199, 999]
          >>> counting_sort([1234, 4321, 3214, 2413])
          [1234, 2413, 3214, 4321]
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

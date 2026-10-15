test = {
  'name': 'max_concurrent',
  'points': 16,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> max_concurrent([('A', 9, 11), ('B', 10, 12), ('C', 11, 13)])
          2
          >>> max_concurrent([('A', 9, 17), ('B', 10, 12), ('C', 10, 11), ('D', 16, 18)])
          3
          >>> max_concurrent([('A', 9, 10), ('B', 10, 11)])
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hw_02 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

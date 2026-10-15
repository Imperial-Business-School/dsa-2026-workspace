test = {
  'name': 'divide',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> divide(10, 2)
          5.0
          >>> divide(10, 0)
          No division by 0.
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from structs_files_errors import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

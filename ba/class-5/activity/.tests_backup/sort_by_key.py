test = {
  'name': 'sort_by_key',
  'points': 14,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sort_by_key([('USA', 4.4, 2.3), ('Japan', 3.2, 2), ('Germany', 4.0, 1), ('China', 4.1, 9), ('Thailand', 2, 1.2), ('Argentina', 9, 2.3), ('Brazil', 10, 1.7)], get_unemployment)
          [('Brazil', 10, 1.7), ('Argentina', 9, 2.3), ('USA', 4.4, 2.3), ('China', 4.1, 9), ('Germany', 4.0, 1), ('Japan', 3.2, 2), ('Thailand', 2, 1.2)]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from sorting import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

test = {
  'name': 'count_characters',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> count_characters('aaaa')
          {'a': 4}
          >>> x = count_characters('test')
          >>> print(x['t'])
          2
          >>> x = count_characters('hello')
          >>> print(x['h'])
          1
          >>> x = count_characters('hello world')
          >>> print(x['l'])
          3
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

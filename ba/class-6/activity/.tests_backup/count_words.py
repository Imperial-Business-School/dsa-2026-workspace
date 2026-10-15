test = {
  'name': 'count_words',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = count_words('test sentence')
          >>> print(x['test'])
          1
          >>> x = count_words('it is what it is')
          >>> print(x['it'])
          2
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

test = {
  'name': 'print_dict_values',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print_dict_values({'Zoe': 'ICL', 'Mark': 'UCL'})
          Mark UCL
          Zoe ICL
          2
          >>> print_dict_values({'banana': 'yellow', 'apple': 'green', 'berry': 'blue'})
          apple green
          banana yellow
          berry blue
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

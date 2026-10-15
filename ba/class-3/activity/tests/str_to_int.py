test = {
  'name': 'str_to_int',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> L = [['Name', 'Favorites'], ['Jay', '100'], ['Jack', '99']]
          >>> y = str_to_int(L, 1)
          >>> print(y)
          [100, 99]
          >>> L = [['Number1', 'Number2'], ['8', '3'], ['7', '5']]
          >>> y = str_to_int(L, 0)
          >>> print(y)
          [8, 7]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from seq_data_extra import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

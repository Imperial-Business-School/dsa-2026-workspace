test = {
  'name': 'count_capital_letters',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> count_capital_letters(['HEY YOU', 'date1', 100, 10, 'id'])
          6
          >>> count_capital_letters(['hey YOU', 'date1', 100, 10, 'id'])
          3
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

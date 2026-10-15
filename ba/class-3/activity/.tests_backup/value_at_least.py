test = {
  'name': 'value_at_least',
  'points': 7,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> tw = [0, 100, 3]
          >>> value_at_least(tw, 2)
          [1, 2]
          >>> value_at_least([4, 1, 5], 5)
          [2]
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

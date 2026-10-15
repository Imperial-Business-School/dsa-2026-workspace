test = {
  'name': 'to_chars',
  'points': 7,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> to_chars('HeLlo!')
          'hello'
          >>> to_chars("Never (1) odd or (2) even...")
          'neveroddoreven'
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

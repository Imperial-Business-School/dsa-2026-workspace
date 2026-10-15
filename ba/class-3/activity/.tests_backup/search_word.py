test = {
  'name': 'search_word',
  'points': 17,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> search_word("searching for a substring", "subway")
          'sub'
          >>> search_word("dog owner", "catdog oh catdog")
          'dog o'
          >>> search_word("fish", "filet")
          'fi'
          >>> search_word("fish", "ballet")
          ''
          >>> search_word("land a plane", "lane")
          'lane'
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

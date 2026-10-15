test = {
  'name': 'longest_item',
  'points': 7,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> longest_item(['hello', 'how', 'are', 'you'])
          0
          >>> longest_item('All happy families are alike'.split())
          2
          >>> x = longest_item('All happy families are alike'.split())
          >>> isinstance(x, int)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from seq_data import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

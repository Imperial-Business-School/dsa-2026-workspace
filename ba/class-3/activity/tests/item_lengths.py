test = {
  'name': 'item_lengths',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> item_lengths(['hello', 'how', 'are', 'you', 'doing'])
          [5, 3, 3, 3, 5]
          >>> item_lengths('All happy families are alike'.split())
          [3, 5, 8, 3, 5]
          >>> x = item_lengths('All happy families are alike'.split())
          >>> x[0]
          3
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

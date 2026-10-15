test = {
  'name': 'HashTable',
  'points': 25,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ht = HashTable(num_buckets=4)
          >>> ht['AAPL'] = 150
          >>> ht['MSFT'] = 300
          >>> ht['AAPL']
          150
          >>> 'MSFT' in ht
          True
          >>> 'GOOG' in ht
          False
          >>> len(ht)
          2
          >>> ht['AAPL'] = 155
          >>> ht['AAPL']
          155
          >>> len(ht)
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hw_02 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

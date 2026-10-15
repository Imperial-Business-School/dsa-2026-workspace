test = {
  'name': 'buy_and_hold',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> res = buy_and_hold([2.0, 1.5, 1.8, 2.3, 2.5])
          >>> [round(x, 1) for x in res]
          [100.0, 75.0, 90.0, 115.0, 125.0]
          >>> [round(x, 2) for x in buy_and_hold([2.0, 1.5, 1.8, 2.3, 2.5], start_index=2)]
          [100.0, 100.0, 100.0, 127.78, 138.89]
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

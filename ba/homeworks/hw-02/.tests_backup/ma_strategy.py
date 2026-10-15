test = {
  'name': 'ma_strategy',
  'points': 9,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> starting_cash = 1.0
          >>> prices = [2,4,6,5,1]
          >>> cos = [0, 1, 1, 0, 0]
          >>> values = ma_strategy(prices, cos, starting_cash)
          >>> values
          [1.0, 1.0, 1.5, 1.25, 1.25]
          >>> starting_cash = 1000.0
          >>> prices = [2,3,4,5,4,3,2,1,6,1,5,7,8,10,7,9]
          >>> cos = [None, None, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
          >>> values = ma_strategy(prices, cos, starting_cash)
          >>> [round(v, 2) for v in values]
          [1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 166.67, 833.33, 833.33, 952.38, 1190.48, 833.33, 1071.43]
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

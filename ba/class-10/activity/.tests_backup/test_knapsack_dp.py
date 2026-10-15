test = {
  'name': 'test_knapsack_dp',
  'points': 30,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> names = ['gold', 'silver', 'bronze']
          >>> values = [60, 100, 120]
          >>> weights = [10, 20, 30]
          >>> items = [Item(n, v, w) for n, v, w in zip(names, values, weights)]
          >>> knapsack_dp(items, 50)
          220.0
          >>> names = ['clock', 'painting', 'radio']
          >>> values = [175, 90, 20]
          >>> weights = [10, 9, 4]
          >>> items = [Item(n, v, w) for n, v, w in zip(names, values, weights)]
          >>> knapsack_dp(items, 13)
          175.0
          >>> knapsack_dp(items, 5)
          20.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from greedy import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

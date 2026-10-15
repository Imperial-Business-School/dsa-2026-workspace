test = {
  'name': 'test_greedy_fractional',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> names = ['clock', 'painting', 'radio']
          >>> values = [175,90,20]
          >>> weights = [10,9,4]
          >>> items = [Item(n, v, w) for n,v,w in zip(names, values, weights)]
          >>> res, val = greedy_fractional(items, 5, density)
          >>> val
          87.5
          >>> res, val = greedy_fractional(items, 13, density)
          >>> val
          205.0
          >>> res, val = greedy_fractional(items, 11, weight_inverse)
          >>> val
          90.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from greedy import *
      >>> from greedy_extra import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

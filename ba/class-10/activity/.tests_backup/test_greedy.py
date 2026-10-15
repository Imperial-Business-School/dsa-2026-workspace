test = {
  'name': 'test_greedy',
  'points': 20,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> names = ['clock', 'painting', 'radio']
          >>> values = [175,90,20]
          >>> weights = [10,9,4]
          >>> items = [Item(n, v, w) for n,v,w in zip(names, values, weights)]
          >>> res, val = greedy(items, 5, density)
          >>> [val, len(res)]
          [20.0, 1]
          >>> res, val = greedy(items, 13, density)
          >>> [val, len(res)]
          [175.0, 1]
          >>> res, val = greedy(items, 13, weight_inverse)
          >>> [val, len(res)]
          [110.0, 2]
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

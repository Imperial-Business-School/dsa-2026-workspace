test = {
  'name': 'q1_recap',
  'points': 14,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def lsum(L):
          ...     # L is a list with at least two items
          ...     list_sum = L[0]
          ...     for item in L[1:]:
          ...         list_sum =  list_sum + item
          ...     print(list_sum)
          >>> lsum([1, 2, 3])
          46b6541dbcee7a4cf1f90c9fd580d1bc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> lsum(['a', 'b', 'c'])
          0e04d81b0e64aeefffdcf4704db21e01
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = lsum([2, 2, 1])
          >>> print(x)
          9d217a80e7225e06121e9b9f0b919379
          6e316ac2d619b3f47fabed9be60b43c9
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'type': 'wwpp'
    }
  ]
}

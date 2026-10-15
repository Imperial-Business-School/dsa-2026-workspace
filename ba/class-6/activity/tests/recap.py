test = {
  'name': 'Recap',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> l1 = [1, 2, 4, 8, 16]
          >>> l2 = [1, 3, 9, 27]
          >>> len(l1)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> l1 = [1, 2, 4, 8, 16]
          >>> l2 = [1, 3, 9, 27]
          >>> len(l2)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> l1 = [1, 2, 4, 8, 16]
          >>> l2 = [1, 3, 9, 27]
          >>> l3_a = [l1, l2]
          >>> len(l3_a)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> l1 = [1, 2, 4, 8, 16]
          >>> l2 = [1, 3, 9, 27]
          >>> l3_b = l1 + l2
          >>> len(l3_b)
          9
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> cnt = 0
          >>> for i in range(9):
          ...     cnt += 1
          >>> print(cnt)
          9
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'type': 'wwpp'
    }
  ]
}

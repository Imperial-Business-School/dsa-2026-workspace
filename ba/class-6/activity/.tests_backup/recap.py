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
          96d40d013e23679fb02f8e16b1ca3ae9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [1, 2, 4, 8, 16]
          >>> l2 = [1, 3, 9, 27]
          >>> len(l2)
          09e15535b274c7b526e57d1a67d97f4c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [1, 2, 4, 8, 16]
          >>> l2 = [1, 3, 9, 27]
          >>> l3_a = [l1, l2]
          >>> len(l3_a)
          2760d308a1982bd76abbb5a2883d31e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [1, 2, 4, 8, 16]
          >>> l2 = [1, 3, 9, 27]
          >>> l3_b = l1 + l2
          >>> len(l3_b)
          02023badfcd182e96431a63561f422e9
          # locked
          """,
          'hidden': False,
          'locked': True
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
          02023badfcd182e96431a63561f422e9
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

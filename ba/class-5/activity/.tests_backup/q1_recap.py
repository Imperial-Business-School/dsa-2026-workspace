test = {
  'name': 'Recap',
  'points': 14,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> a = [2, 2, 3, 1]
          >>> b = []
          >>> for i in a:
          >>>   b.append(i**2)
          >>> b # enter lists in format [a, b, c, d] including spaces
          4520f6bcfd70186a62ee454f7fca1a3e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def calculate(x):
          >>>     return len(x)
          >>> a = ['a','A','er','cere']
          >>> b = []
          >>> for i in a:
          >>>   b.append(calculate(i))
          >>> b
          43fac8090c79548939679fd8f01cde50
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> a = [3, 6, 8, 7]
          >>> b = []
          >>> for i in range(len(a)):
          >>>   b.append(a[len(a)-1-i])
          >>> b
          21dac6d41af14be9ee6309148e75e763
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
          >>> a = [3, 6, 8, 1, 78, 2, 23, 45, 9]
          >>> x = 2
          >>> def f(s, i):
          ...     for elem in s:          
          ...         if elem == i:
          ...             return True
          ...     return False
          >>> f(a, x)
          52695826e13fbc9d10f0f7993247d254
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
          'answer': 'ae85264f258195e3b0fec8dd096ab84b',
          'choices': [
            'O(n)',
            'O(n**3)',
            'O(n**2)',
            'O(n*log(n))'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What is the complexity of the previous code? (if n = len(a)):'
        }
      ],
      'scored': True,
      'type': 'concept'
    }
  ]
}

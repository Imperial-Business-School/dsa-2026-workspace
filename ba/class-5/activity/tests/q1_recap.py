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
          [4, 4, 9, 1]
          """,
          'hidden': False,
          'locked': False
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
          [1, 1, 2, 4]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> a = [3, 6, 8, 7]
          >>> b = []
          >>> for i in range(len(a)):
          >>>   b.append(a[len(a)-1-i])
          >>> b
          [7, 8, 6, 3]
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
          >>> a = [3, 6, 8, 1, 78, 2, 23, 45, 9]
          >>> x = 2
          >>> def f(s, i):
          ...     for elem in s:          
          ...         if elem == i:
          ...             return True
          ...     return False
          >>> f(a, x)
          True
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
          'answer': 'O(n)',
          'choices': [
            'O(n)',
            'O(n**3)',
            'O(n**2)',
            'O(n*log(n))'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What is the complexity of the previous code? (if n = len(a)):'
        }
      ],
      'scored': True,
      'type': 'concept'
    }
  ]
}

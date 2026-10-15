test = {
  'name': 'Recap',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> d = {'dog', 'cat', 'bird', 'cow'}
          >>> type(d)
          57b7c912fd8e411c9a07f7fc58c1bb91
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> 'cat' in d
          70a50a5a98926d4029cce48410554547
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> d.add('mouse')
          >>> len(d)
          0ea5b037c780e28ecb4d0e3507dea50a
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
          >>> # Write Error if there's an error
          >>> x, y = [9,3,1], 1 
          >>> y
          b9509e670ba3c81eaa17a34507ee3b3b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Write Error if there's an error
          >>> x, y = 4, 1 
          >>> y, x = x, y 
          >>> x
          b9509e670ba3c81eaa17a34507ee3b3b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Write Error if there's an error
          >>> def f(x, y):
          ...     a, b = 3*x, 2*y
          ...     return a, b
          >>> x, y = f(2, 2)
          >>> x
          26512e2c8fbce288cb2560b16f37741f
          # locked
          >>> y
          324385caec9f65bade73f864596137c3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> animals = {'eagle': 'bird', 'hawk': 'bird', 'manatee': 'mammal', 'finch': 'bird'}
          >>> bird_count = 0
          >>> for animal in animals:
          ...    if animals[animal] == 'bird':
          ...        bird_count += 1
          >>> bird_count
          75dfaeffc0c9a90182d43468a629e16a
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

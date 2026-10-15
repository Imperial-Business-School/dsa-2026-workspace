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
          set
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 'cat' in d
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> d.add('mouse')
          >>> len(d)
          5
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
          >>> # Write Error if there's an error
          >>> x, y = [9,3,1], 1 
          >>> y
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Write Error if there's an error
          >>> x, y = 4, 1 
          >>> y, x = x, y 
          >>> x
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Write Error if there's an error
          >>> def f(x, y):
          ...     a, b = 3*x, 2*y
          ...     return a, b
          >>> x, y = f(2, 2)
          >>> x
          6
          >>> y
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> animals = {'eagle': 'bird', 'hawk': 'bird', 'manatee': 'mammal', 'finch': 'bird'}
          >>> bird_count = 0
          >>> for animal in animals:
          ...    if animals[animal] == 'bird':
          ...        bird_count += 1
          >>> bird_count
          3
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

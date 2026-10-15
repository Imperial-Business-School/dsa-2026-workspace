test = {
  'name': 'Comprehensions',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> [x**2 for x in range(2)]
          [0, 1]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> [len(name) for name in ['Joe', 'Mary', 'Zoe']]
          [3, 4, 3]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> names = {name:len(name) for name in ['John', 'Mary', 'Zoe']}
          >>> names['Zoe']
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> names = [name:len(name) for name in ['John', 'Mary', 'Zoe']]
          >>> names['Zoe']
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> x = {s for s in 'John'}
          >>> 'j' in x
          False
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

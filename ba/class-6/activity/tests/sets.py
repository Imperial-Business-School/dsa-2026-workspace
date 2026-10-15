test = {
  'name': 'Sets and tuples',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> cities = set()
          >>> cities.add('London')
          >>> cities.add('Paris')
          >>> 'Rome' in cities
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cities = ('London', 'Paris', 'Rome')
          >>> cities.add('Amsterdam')
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cities = ('London', 'Paris', 'Rome')
          >>> cities.append('Amsterdam')
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cities = ('London', 'Paris', 'Rome')
          >>> cities[0] = 'Amsterdam'
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def sum_and_difference(x, y):
          ...     return x + y, x - y
          >>> z = sum_and_difference(5, 3)
          >>> type(z)
          tuple
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def sum_and_difference(x, y):
          ...     return x + y, x - y
          >>> z, w = sum_and_difference(5, 3)
          >>> type(z)
          int
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

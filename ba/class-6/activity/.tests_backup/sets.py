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
          6f112e0776e191b5e4dfb1ceb0fd2e17
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> cities = ('London', 'Paris', 'Rome')
          >>> cities.add('Amsterdam')
          a400bf129e1bfa94407e754f6f790095
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> cities = ('London', 'Paris', 'Rome')
          >>> cities.append('Amsterdam')
          a400bf129e1bfa94407e754f6f790095
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> cities = ('London', 'Paris', 'Rome')
          >>> cities[0] = 'Amsterdam'
          a400bf129e1bfa94407e754f6f790095
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def sum_and_difference(x, y):
          ...     return x + y, x - y
          >>> z = sum_and_difference(5, 3)
          >>> type(z)
          b34dcf81c57ab182673cb5007ca61ea2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def sum_and_difference(x, y):
          ...     return x + y, x - y
          >>> z, w = sum_and_difference(5, 3)
          >>> type(z)
          afb5335dcd497e4f1d159b4c616d2652
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

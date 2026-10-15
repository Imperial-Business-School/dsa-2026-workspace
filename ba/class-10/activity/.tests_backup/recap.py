test = {
  'name': 'Recap',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def f(x):
          ...     y = x - 1
          ...     z = y*2
          ...     return y + z
          >>> y = 1
          >>> z = 2
          >>> x = 3
          >>> y = f(z + x)
          >>> print(x, y, z)
          4e320aed78461db9fd4ebfd1ee30e06d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def g(x):
          ...     y = x - 1
          ...     return y
          ...     z = y*2
          ...     return y + z
          >>> x = 1
          >>> y = g(x)
          >>> y
          cd3625ba3ccc97b717418860fb4683e1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = 1
          >>> while x<=8 or x%2==0:
          ...     x = x+3
          ...     print(x)
          661176b5d413910d990ebddad5ca7d53
          1bba8a842ac627ed53c833f73818b0db
          710b5215e888c1f356221b7cfd4a2e0f
          4739b80ee518a7798ded29ddb5228299
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

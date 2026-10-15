test = {
  'name': 'Comparisons',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(2 > 2)
          69276c42186bbd1e98ee3791f286fcde
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print(2 >= 2)
          0b83116f73762a3ad398f1db5c594269
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print(not (5 > 2))
          69276c42186bbd1e98ee3791f286fcde
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = 5
          >>> y = 4
          >>> print(x > y and x < 8)
          0b83116f73762a3ad398f1db5c594269
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

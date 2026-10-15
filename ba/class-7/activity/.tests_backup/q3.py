test = {
  'name': 'Numpy - Q3',
  'points': 6,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # fb_returns.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell above this test cell where you defined
          >>> # fb_returns.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'fb_returns' in vars()
          a7465ecc0421c9e0085a8a012fce1e93
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> sum(fb_returns)//0.0001 == 3212.0
          716f84bd25b74b06e654f453c6b2b389
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

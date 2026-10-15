test = {
  'name': 'Pandas_Q5',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # reduced_data.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell above this test cell where you defined
          >>> # reduced_data.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'reduced_data' in vars()
          cef461e340f176db84632b8704478459
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> reduced_data.shape[1] == 9
          cef461e340f176db84632b8704478459
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> reduced_data.shape[0] == 891
          cef461e340f176db84632b8704478459
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # It looks like the columns requested to be removed
          >>> # do still exist.
          >>> exists = False
          >>> if 'Cabin' in reduced_data.columns: 
          ...     exists = True
          >>> exists
          6f112e0776e191b5e4dfb1ceb0fd2e17
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

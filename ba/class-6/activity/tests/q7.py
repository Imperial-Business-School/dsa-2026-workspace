test = {
  'name': 'Pandas_Q7',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # only_pclass2.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell above this test cell where you defined
          >>> # only_pclass2.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'only_pclass2' in vars()
          cef461e340f176db84632b8704478459
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> only_pclass2.shape[1] == 13
          cef461e340f176db84632b8704478459
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> only_pclass2.shape[0] == 184
          cef461e340f176db84632b8704478459
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Ensure that there are no passengers with Pclass = 2.
          >>> d1 = only_pclass2
          >>> check_class2 = d1['Pclass'].where(d1['Pclass'] == 2, other=-1).value_counts()
          >>> bool(check_class2.values[0] == only_pclass2.shape[0])
          cef461e340f176db84632b8704478459
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

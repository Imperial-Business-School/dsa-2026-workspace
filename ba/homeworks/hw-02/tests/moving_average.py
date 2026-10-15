test = {
  'name': 'moving_average',
  'points': 9,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ma = moving_average([2,3,4,5,8,5,4,3,2,1], 3)
          >>> [round(m, 2) if m is not None else None for m in ma]
          [None, None, 3.0, 4.0, 5.67, 6.0, 5.67, 4.0, 3.0, 2.0]
          >>> moving_average([2,3,4,5,8,5,4,3,2,1], 2)
          [None, 2.5, 3.5, 4.5, 6.5, 6.5, 4.5, 3.5, 2.5, 1.5]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hw_02 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

test = {
  'name': 'total_duration',
  'points': 19,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> mixtape_durations = [
          ...     [180, 210, 195],
          ...     [220, [175, 205]],
          ...     240,
          ... ]
          >>> total_duration(mixtape_durations)
          1425
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hw_01 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

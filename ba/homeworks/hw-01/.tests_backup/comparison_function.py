test = {
  'name': 'comparison_function',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> comparison_function(99) > comparison_function(18783479)
          True
          >>> comparison_function(123) > comparison_function(321)
          False
          >>> comparison_function(1789) > comparison_function(96861)
          True
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

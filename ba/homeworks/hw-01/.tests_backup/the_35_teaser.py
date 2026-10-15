test = {
  'name': 'the_35_teaser',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> the_35_teaser(9)
          '3'
          >>> the_35_teaser(95)
          '5'
          >>> the_35_teaser(300)
          '35'
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
